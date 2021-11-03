import names
import random
import requests
from lorem_text import lorem
from error.exceptions import RequiredParamError, OptionFormatError
from datetime import datetime, date, timedelta

def generate_fake_data(schema, data_count, include_index=False):
    response = []
    for i in range(int(data_count)):
        jsn_response = {}

        if include_index:
            jsn_response['_id'] = i

        for key, value in schema.items():
            jsn_response[key] = generate_fake_value(value)
        response.append(jsn_response)
    return response

def get_data_cmd_dict():
    return {
        'first_name': create_first_name,
        'last_name': create_last_name,
        'full_name': create_full_name,
        'email': create_email,
        'sentence': create_sentence,
        'paragraph': create_paragraph,
        'words': create_words,
        'enum': create_enum,
        'integer': create_integer,
        'boolean': create_boolean,
        'decimal': create_decimal,
        'image_url': create_image_url,
        'datetime': create_datetime,
        'date': create_date
    }

def generate_fake_value(value):
    data_type = value['type']
    options = value['options'] if 'options' in value else {}
    cmd_function = get_data_cmd_dict()[data_type]
    return cmd_function(options)

def create_first_name(options):
    gender = options['gender'] if 'gender' in options else None
    return names.get_first_name(gender=gender)

def create_last_name(options):
    return names.get_last_name()

def create_full_name(options):
    first_name = create_first_name(options)
    last_name = create_last_name(options)
    return f'{first_name} {last_name}'

def create_email(options):
    gender = options['gender'] if 'gender' in options else None
    full_name = names.get_full_name(gender=gender)
    formatted_name = full_name.replace(' ','').lower()
    email_num = random.randint(1000, 9999)
    return f'{formatted_name}{email_num}@email.com'

def create_sentence(options):
    return lorem.sentence()

def create_paragraph(options):
    if 'paragraph_length' in options:
        paragraph_length = options['paragraph_length']

        if not isinstance(paragraph_length, int):
            raise OptionFormatError('paragraph_length type must be an integer')
        return lorem.paragraphs(paragraph_length)
    return lorem.paragraph()

def create_words(options):
    if 'word_length' not in options:
        raise RequiredParamError('word_length')

    word_length = options['word_length']

    if not isinstance(word_length, int):
        raise OptionFormatError('word_length type must be an integer')
    return lorem.words(word_length)

def create_enum(options):
    # check for required option params
    if 'values' not in options:
        raise RequiredParamError('values')

    selections = options['values']

    # check for option param format
    if not isinstance(selections, list):
        raise OptionFormatError('values type must be an array')

    return random.choice(selections)

def create_integer(options):
    # check for required option params
    if 'range' not in options:
        raise RequiredParamError('range')

    range = options['range']

    # check for option param format
    if not isinstance(range, list):
        raise OptionFormatError('range type must be an array')
    if len(range) != 2 or range[0] > range[1]:
        raise OptionFormatError('range format should be [<min_number>, <max_number>]')

    min_number = range[0]
    max_number = range[1]
    return random.randint(min_number, max_number)

def create_decimal(options):
    # check for required option params
    if 'decimal_places' not in options:
        raise RequiredParamError('decimal_places')
    if 'range' not in options:
        raise RequiredParamError('range')

    decimal_places = options['decimal_places']
    range = options['range']

    # check for option param format
    if not isinstance(range, list):
        raise OptionFormatError('range type must be an array')
    if len(range) != 2 or range[0] > range[1]:
        raise OptionFormatError('range format should be [<min_number>, <max_number>]')

    min_number = range[0]
    max_number = range[1]
    return round(random.uniform(min_number, max_number), decimal_places)

def create_boolean(options):
    return bool(random.getrandbits(1))

def create_image_url(options):
    if 'category' not in options:
        raise RequiredParamError('category')

    category = options['category']
    width = options['width'] if 'width' in options else 1080

    if not isinstance(width, int):
        raise OptionFormatError('width should be an integer')

    r = requests.get(f'https://unsplash.com/napi/search/photos?query={category}&per_page=100')
    results = r.json()['results']

    random_index = random.randint(0, len(results))
    image_url = results[random_index]['urls']['regular']
    return image_url.replace('w=1080', f'w={width}')

def create_datetime(options):
    if 'range' not in options:
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    range = options['range']

    if not isinstance(range, list):
        raise OptionFormatError('range should be an array')
    if len(range) != 2 or range[0] > range[1]:
        raise OptionFormatError('range format should be [<start_datetime>, <end_datetime>]')

    try:
        start_datetime = datetime.strptime(range[0], '%Y-%m-%d %H:%M:%S')
        end_datetime = datetime.strptime(range[1], '%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        raise OptionFormatError(str(e))

    delta = end_datetime - start_datetime
    int_delta = delta.total_seconds()

    # return the start_date/end_date if they have the same value
    if int_delta == 0.0:
        return start_datetime.strftime('%Y-%m-%d %H:%M:%S')

    random_second = random.randrange(int_delta)
    random_datetime = start_datetime + timedelta(seconds=random_second)
    return random_datetime.strftime('%Y-%m-%d %H:%M:%S')

def create_date(options):
    if 'range' not in options:
        return date.today().strftime('%Y-%m-%d')

    range = options['range']

    if not isinstance(range, list):
        raise OptionFormatError('range should be an array')
    if len(range) != 2 or range[0] > range[1]:
        raise OptionFormatError('range format should be [<start_date>, <end_date>]')

    try:
        start_date = datetime.strptime(range[0], '%Y-%m-%d')
        end_date = datetime.strptime(range[1], '%Y-%m-%d')
    except ValueError as e:
        raise OptionFormatError(str(e))

    delta = end_date - start_date
    int_delta = delta.total_seconds()

    # return the start_date/end_date if they have the same value
    if int_delta == 0.0:
        return start_date.strftime('%Y-%m-%d')

    random_second = random.randrange(int_delta)
    random_date = start_date + timedelta(seconds=random_second)
    return random_date.strftime('%Y-%m-%d')
