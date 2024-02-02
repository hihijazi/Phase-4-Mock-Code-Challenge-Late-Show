from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    air_date = db.Column(db.String)  # Assuming the air date is stored as a string
    episode_number = db.Column(db.Integer)

    # Add relationship
    appearances = db.relationship("Appearance", back_populates="episode")

    # Add serialization
    serialize_rules = ("-appearances.episode",)

    def __repr__(self):
        return f"<Episode {self.id} : {self.air_date}, {self.episode_number}>"



class Guest(db.Model, SerializerMixin):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # Add relationship
    appearance = db.relationship("Appearance", back_populates="guest")  
  
    # Add serialization
    serialize_rules = ("-appearance.guest",)

    def __repr__(self):
        return f"<Guest {self.id} : {self.name}>"

class Appearance(db.Model, SerializerMixin):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'))    
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))    

    # Add relationships
    episode = db.relationship("Episode", back_populates="appearances")  
    guest = db.relationship("Guest", back_populates="appearance")   

    #Add serialization
    serialize_rules = ("-guest.appearance",)

    # Add validation
    @validates('rating')
    def validate_rating(self, key, value):
        if value is None:
            raise ValueError('Must have a rating between 1 and 5 ')
        return value

    def __repr__(self): 
        return f"<Appearance {self.id} : {self.episode_id} : {self.guest_id}>"  
    



# add any models you may need. 