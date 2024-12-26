from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/login', methods=['POST'])
def receive_data():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == 'admin':
        return jsonify({'message': 'failed'}), 401

    return jsonify({'message': f'hello {username} you are login successfully'})    



if __name__ == '__main__':
    app.run(port=5000)