#!/usr/bin/python3

"""
This script adds the State object "Louisiana"hbtn_0e_6_usa database
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == '__main__':

    #  Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    #  Database connection URI
    DATABASE_URI = f'mysql://{username}:{password}@localhost:3360/{database_name}'
    engine = create_engine(DATABASE_URI)

    #  Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    #  Create a new State object for Louisiana
    new_state = State(name="Louisiana")

    #  Add the new state to the database
    session.add(new_state)
    session.commit()

    #  Print the new state's ID
    print(new_state.id)

    #  free resources
    session.close()
