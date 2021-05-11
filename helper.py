import names
import random
from lorem_text import lorem

def generate_fake_data(schema, data_count):
    response = []
    for i in range(int(data_count)):
        jsn_response = {}
        for key, value in schema.items():
            jsn_response[key] = generate_fake_value(value)
        response.append(jsn_response)

    return response

def get_data_cmd_dict():
    test = {
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
        'decimal': create_decimal
    }
    return test

def generate_fake_value(value):
    data_type = value['type']
    options = value['options'] if 'options' in value else {}
    cmd_function = get_data_cmd_dict()[data_type]
    return cmd_function(options)

def create_first_name(options):
    if 'gender' in options:
        gender = options['gender']
        return names.get_first_name(gender=gender)
    return names.get_first_name()

def create_last_name(options):
    return names.get_last_name()

def create_full_name(options):
    if 'gender' in options:
        gender = options['gender']
        return names.get_full_name(gender=gender)
    return names.get_full_name()

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
        return lorem.paragraphs(paragraph_length)
    return lorem.paragraph()

def create_words(options):
    if 'word_length' not in options:
        raise MyException('word_length is required')

    word_length = options['word_length']
    return lorem.words(word_length)

def create_enum(options):
    # check for required option params
    if 'values' not in options:
        raise MyException('values is required')

    selections = options['values']

    # check for option param format
    if not isinstance(selections, list):
        raise MyException('values type must be an array')

    return random.choice(selections)

def create_integer(options):
    # check for required option params
    if 'range' not in options:
        raise MyException('range is required')

    range = options['range']

    # check for option param format
    if not isinstance(range, list):
        raise MyException('range type must be an array')
    if len(range) != 2:
        raise MyException('range format should be [<min_number>, <max_number>]')

    min_number = range[0]
    max_number = range[1]
    return random.randint(min_number, max_number)

def create_decimal(options):
    # check for required option params
    if 'decimal_places' not in options:
        raise MyException('decimal_places is required')
    if 'range' not in options:
        raise MyException('range is required')

    decimal_places = options['decimal_places']
    range = options['range']

    # check for option param format
    if not isinstance(range, list):
        raise MyException('range type must be an array')
    if len(range) != 2:
        raise MyException('range format should be [<min_number>, <max_number>]')

    min_number = range[0]
    max_number = range[1]
    test = round(random.uniform(min_number, max_number), decimal_places)
    return test

def create_boolean(options):
    return bool(random.getrandbits(1))
