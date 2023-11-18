import json
from models import Workouts
from database import db

def load_workouts_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    for workout in data:
        new_workout = Workouts(
            id=workout['id'],
            name=workout['name'],
            title=workout['title'],
            difficulty=workout['difficulty'],
            image_link=workout.get('gif'),  # Use .get() to avoid KeyError if the key doesn't exist
            youtube_link=workout.get('link'),
            solution=json.dumps(workout.get('solution')),  # Convert the 'solution' dict to a JSON string
            template=json.dumps(workout.get('template')),  # The JSON data doesn't seem to have a 'template' field
            filter=['react'],  # Set the 'filter' field to ['react']
            checklist=workout.get('checkList')
        )
        db.session.add(new_workout)

    db.session.commit()