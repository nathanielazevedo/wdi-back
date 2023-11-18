from sqlalchemy import Column, Integer, String, Text, ARRAY
from database import db  # Import the db instance from database.py

class Workouts(db.Model):  # Inherit from db.Model
    __tablename__ = 'workouts'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    title = Column(String(255))
    difficulty = Column(String(50))
    image_link = Column(String(255))
    youtube_link = Column(String(255))
    solution = Column(Text)
    template = Column(Text)
    filter = Column(ARRAY(Text))
    checklist = Column(ARRAY(Text))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'title': self.title,
            'difficulty': self.difficulty,
            'image_link': self.image_link,
            'youtube_link': self.youtube_link,
            'solution': self.solution,
            'template': self.template,
            'filter': self.filter,
            'checklist': self.checklist
        }