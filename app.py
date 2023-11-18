from flask import Flask, jsonify
from flask_cors import CORS
from database import db  # Import the db instance from database.py
from models import Workouts  # Import the Workouts model
from addToDb import load_workouts_from_json  # Import the load_workouts_from_json function
from secret import get_secret  
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in the app
secret = get_secret()
secret_dict = json.loads(secret)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{secret_dict['username']}:{secret_dict['password']}@{secret_dict['host']}:{secret_dict['port']}/postgres"

db.init_app(app)  # Initialize the db instance with the app

@app.route('/')
def hello_nate():
    return 'Hey Nate'

@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workouts.query.all()
    workouts_list = [workout.to_dict() for workout in workouts]
    return jsonify(workouts_list)

@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workouts.query.get(id)
    if workout is None:
        return jsonify({'message': 'Workout not found'}), 404
    return jsonify(workout.to_dict()), 200

# @app.route('/load_workouts', methods=['GET'])
# def load_workouts():
#     file_path = './workouts.json'  # Replace with the actual path to your JSON file
#     load_workouts_from_json(file_path)
#     return jsonify({'message': 'Workouts loaded successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)