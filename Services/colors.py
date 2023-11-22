from sqlalchemy.orm import Session
from Models.attributes import Attribute
from engine import engine


def get_colors():
    with Session(engine) as session:
        # Récupérer la liste des utilisateurs
        colors = session.query(Attribute).all()
        session.close()
    return colors


def set_color(value):
    with Session(engine) as session:
        # Ajouter un nouvel utilisateur à la base de données
        new_color = Attribute(type='COLOR', value=value)
        session.add(new_color)
        session.commit()
        session.close()
    return new_color
