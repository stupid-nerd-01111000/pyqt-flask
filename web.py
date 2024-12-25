from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/')
def send_data():
    return '<p>hello</p>'


@app.route('/receive', methods=[POST])
def receive_data():
    data = request.json
    return jsonify({'status': 'success'})
    



if __name__ == '__main__':
    app.run(port=5000)