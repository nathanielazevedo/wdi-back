from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in the app

@app.route('/')
def hello_nate():
    return 'Hey Nate'

if __name__ == '__main__':
    app.run(debug=True)