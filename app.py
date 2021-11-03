import names
import random
from helper import generate_fake_data
from flask import Flask, jsonify, request
from error.handlers import get_exception_response_and_code
from error.exceptions import EmptyRequestError

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    response = {'status': 'up'}
    return jsonify(response), 200

@app.route('/users/<user_count>', methods=['GET'])
def get_fake_users(user_count=None):
    gender_preference = request.args.get('gender')
    users = []
    for i in range(int(user_count)):
        gender = get_gender(gender_preference)
        first_name = names.get_first_name(gender=gender)
        last_name = names.get_last_name()
        user = {
            'name':  {
                'first': first_name,
                'last': last_name,
                'full': f'{first_name} {last_name}'
            },
            'gender': gender,
            'contact': {
                'email': get_email(first_name, last_name)
            }
        }
        users.append(user)
    return jsonify(users), 200

@app.route('/get_fake_data/<data_count>', methods=['GET'])
def get_fake_data(data_count=None):
    json_request = request.get_json()
    try:
        if (json_request == None):
            raise EmptyRequestError

        response = generate_fake_data(json_request, data_count)
        return jsonify(response), 200
    except Exception as e:
        response, code = get_exception_response_and_code(e)
        return jsonify(response), code

def get_gender(gender_preference):
    if gender_preference:
        return gender_preference

    gender = {
        1: 'male',
        2: 'female'
    }
    return gender[random.randint(1, 2)]

def get_email(first_name, last_name):
    user_email_name = f'{first_name.lower()}{last_name.lower()}'
    return f'{user_email_name}@email.com'

if __name__ == '__main__':
    app.run()
