from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    response = {'status': 'up'}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run()
