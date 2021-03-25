import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
from sqlalchemy import DateTime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    iduser = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password= Column(String(50), primary_key=True)

class Personaje(Base):
    __tablename__ = 'personaje'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    idpersonaje = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height= Column(Integer, primary_key=True)
    mass= Column(Integer, primary_key=True)
    hair_color= Column(String(50), nullable=False)
    skin_color= Column(String(50), nullable=False)
    eye_color= Column(String(50), nullable=False)
    birth_year= Column(String(50), nullable=False)
    gender= Column(String(50), nullable=False)
    created= Column(DateTime, nullable=False)
    edited= Column(DateTime, nullable=False)
    homeworld= Column(String(250), nullable=False)
    url= Column(String(250), nullable=False)

class Favpersonaje(Base):
    __tablename__ = 'favpersonaje'
    idfavper= Column(Integer, primary_key=True)
    idpersonaje = Column(Integer, ForeignKey('personaje.idpersonaje'))
    personaje = relationship(Personaje)
    iduser = Column(Integer, ForeignKey('usuario.iduser'))
    usuario = relationship(Usuario)

class Planeta(Base):
    __tablename__ = 'planeta'
    idplaneta = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter= Column(Integer, nullable=False)
    rotation_period= Column(Integer, nullable=False)
    orbital_period= Column(Integer, nullable=False)
    gravity= Column(String(50), nullable=False)
    population= Column(Integer, nullable=False)
    climate= Column(String(50), nullable=False)
    terrain= Column(String(50), nullable=False)
    surface_water= Column(Integer, nullable=False)
    created= Column(DateTime, nullable=False)
    edited= Column(DateTime, nullable=False)
    url= Column(String(250), nullable=False)

class Favplaneta(Base):
    __tablename__ = 'favplaneta'
    idfavpla= Column(Integer, primary_key=True)
    idplaneta = Column(Integer, ForeignKey('planeta.idplaneta'))
    planeta = relationship(Planeta)
    iduser = Column(Integer, ForeignKey('usuario.iduser'))
    usuario = relationship(Usuario)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')