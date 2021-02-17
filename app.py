from flask import Flask
PORT = 8080
DEBUG = True

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!!'






if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
