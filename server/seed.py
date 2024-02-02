#!/usr/bin/env python3

import csv
from random import randint

from app import app
from models import db, Episode, Guest, Appearance

def clear_database():
    with app.app_context():
        Episode.query.delete()
        Guest.query.delete()
        Appearance.query.delete()
        db.session.commit()

def create_episodes(rows):
    with app.app_context():
        episodes = []
        for i, row in enumerate(rows):
            e = Episode(date=row[2], number=i + 1)  # Adjust index to start from 1
            episodes.append(e)
        db.session.add_all(episodes)
        db.session.commit()
    return episodes

def create_guests(rows):
    with app.app_context():
        guests = []
        for i, row in enumerate(rows):
            g = Guest(name=row[-1], occupation=row[1])  # Adjust index to start from 0
            guests.append(g)
        db.session.add_all(guests)
        db.session.commit()
    return guests

def create_appearances(rows, episodes, guests):
    with app.app_context():
        appearances = []
        for row in rows:
            guest_name = row[-1]
            episode_date = row[2]
            guest = Guest.query.filter_by(name=guest_name).first()
            episode = Episode.query.filter_by(date=episode_date).first()
            if guest and episode:
                a = Appearance(rating=randint(1, 5), guest=guest, episode=episode)
                appearances.append(a)
        db.session.add_all(appearances)
        db.session.commit()



if __name__ == '__main__':

    print("Clearing database...")
    clear_database()

    print("Opening CSV...")
    with open('server/seed.csv', newline='') as csvfile:
        rows = [row for row in csv.reader(csvfile, delimiter=',', quotechar='|')]
        print("Seeding episodes...")
        episodes = create_episodes(rows)
        print("Seeding guests...")
        guests = create_guests(rows)
        print("Seeding appearances...")
        create_appearances(rows, episodes, guests)
        print("Complete!")
