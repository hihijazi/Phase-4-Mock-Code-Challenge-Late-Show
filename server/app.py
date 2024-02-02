#!/usr/bin/env python3

from flask import Flask, request
from flask_migrate import Migrate

from models import db, Episode, Guest, Appearance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return 'Mock Code Challenge LATE SHOW'

#Guest Routes 

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return app.json.dumps(guests)

@app.route('/guests', methods=['POST'])
def create_guest():
    data = request.get_json()
    guest = Guest(name=data['name'], email=data['email'])
    db.session.add(guest)
    db.session.commit()
    return app.json.dumps(guest)

@app.route('/guests/<int:id>', methods=['GET'])
def get_guest(id):
    guest = Guest.query.get(id)
    return app.json.dumps(guest)

@app.route('/guests/<int:id>', methods=['PUT'])
def update_guest(id):
    data = request.get_json()
    guest = Guest.query.get(id)
    guest.name = data['name']
    guest.email = data['email']
    db.session.commit()
    return app.json.dumps(guest)

@app.route('/guests/<int:id>', methods=['DELETE'])
def delete_guest(id):
    guest = Guest.query.get(id)
    db.session.delete(guest)
    db.session.commit()
    return app.json.dumps(guest)
    
#Episode Routes
@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return app.json.dumps(episodes)

@app.route('/episodes', methods=['POST'])
def create_episode():
    data = request.get_json()
    episode = Episode(title=data['title'], description=data['description'])
    db.session.add(episode)
    db.session.commit()
    return app.json.dumps(episode)

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    return app.json.dumps(episode)

@app.route('/episodes/<int:id>', methods=['PUT'])
def update_episode(id):
    data = request.get_json()
    episode = Episode.query.get(id)
    episode.title = data['title']
    episode.description = data['description']
    db.session.commit()
    return app.json.dumps(episode)

@app.route('/episodes/<int:id>', methods=['DELETE'])
def delete_episode(id):
    episode = Episode.query.get(id)
    db.session.delete(episode)
    db.session.commit()
    return app.json.dumps(episode)


#Appearance Routes
@app.route('/appearances', methods=['GET'])
def get_appearances():
    appearances = Appearance.query.all()
    return app.json.dumps(appearances)

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    appearance = Appearance(guest_id=data['guest_id'], episode_id=data['episode_id'])
    db.session.add(appearance)
    db.session.commit()
    return app.json.dumps(appearance)

@app.route('/appearances/<int:id>', methods=['GET'])
def get_appearance(id):
    appearance = Appearance.query.get(id)
    return app.json.dumps(appearance)

@app.route('/appearances/<int:id>', methods=['PUT'])
def update_appearance(id):
    data = request.get_json()
    appearance = Appearance.query.get(id)
    appearance.guest_id = data['guest_id']
    appearance.episode_id = data['episode_id']
    db.session.commit()
    return app.json.dumps(appearance)

@app.route('/appearances/<int:id>', methods=['DELETE'])
def delete_appearance(id):
    appearance = Appearance.query.get(id)
    db.session.delete(appearance)
    db.session.commit()
    return app.json.dumps(appearance)


if __name__ == '__main__':
    app.run(port=5555, debug=True)

