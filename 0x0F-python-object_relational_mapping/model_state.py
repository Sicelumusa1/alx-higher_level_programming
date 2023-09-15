#!/usr/bin/python3
"""
Defines a SQLAlchemy model for the "states" table in a MySQL database
Creates the "State" class representing the table and generate in the database
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,String,Integer,create_engine


DATABASE_URI = 'mysql://root:root@localhost:3360/hbtn_0e_6_usa'
engine=create_engine(DATABASE_URI)

Base=declarative_base()

class State(Base):
    """
    Represents the "States" table in the database.
    """
    __tablename__='states'
    id=Column(Integer(),unique=True,nullable=False,primary_key=True,autoincrement=True)
    name=Column(String(128),nullable=False)

    def __init__(self, name):
        """
        Initializes a new state object with a given name.
        """
        self.name = name

if __name__ == '__main__':
    Base.metadata.create_all(engine)
