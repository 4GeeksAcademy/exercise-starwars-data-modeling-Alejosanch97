import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    favourites = relationship("Favourites", backref='User')

class Favourites(Base):
  __tablename__ = "favourites"
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('user.id'))
  vehicles_id = Column(Integer, ForeignKey("vehicles.id"))
  planets_id = Column(Integer, ForeignKey("planets.id"))
  char_id = Column(Integer, ForeignKey("character.id"))

 

class Character(Base):
    __tablename__ = "character"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(50), nullable=False)
    skin_color = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    birth_year = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    created = Column(String(50), nullable=False)
    edited = Column(String(50), nullable=False)
    description = Column(String(1000), nullable=False)
    # asignamos una relación muchos a muchos, pues un personaje puede pilotar mucho vehcles y un vehicle puede ser pilotado por muchos personajes
    piloted_vehicles = relationship("Pilots", back_populates="character")
    # asignamos una relación uno a mucho, pues un personaje tiene un solo planeta de origen y un planeta puede ser el hogar de uno o muchos personajes)
    homeworld = relationship("Planets", backref = "character")
    character_fav = relationship("Favourites", backref = "character")
    

class Vehicles(Base):
    __tablename__ = "vehicles"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    vehicle_class = Column(String(50), nullable=False)
    manufacturer = Column(String(50), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    max_atmosphering_speed = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(50), nullable=False)
    created = Column(String(50), nullable=False)
    edited = Column(String(1000), nullable=False)
    description = Column(String(1000), nullable=False)
    #la relacion es 1 a 1 pues necesitamos garantizar la integridad de los datos. 
    # Cada registro en pilots debe estar asociado a un único vehículo y a un único personaje. 
    # Esto evita redundancias y ambigüedades en la información.
    pilots = relationship("Pilots", backref="vehicle")
    planets = relationship("Planets", backref = "vehicles")
    vehicle_fav = relationship("Favourites", backref = "vehicles")
   

class Planets(Base):
    __tablename__ = "planets"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    surface_water = Column(Integer, nullable=False)
    created = Column(String(50), nullable=False)
    edited = Column(String(50), nullable=False)
    description = Column(String(1000), nullable=False)
    cha_id = Column(String(255), ForeignKey("character.id"))
    vehi_id = Column(String(255), ForeignKey("vehicles.id"))
    planets_fav = relationship("Favourites", backref = "planets")
   
   
class Pilots(Base):
    __tablename__ = "pilots"
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    pilots_to = Column(Integer, ForeignKey("vehicles.id"), primary_key=True)   



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
