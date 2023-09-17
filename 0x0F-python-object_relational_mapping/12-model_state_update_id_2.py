#!/usr/bin/python3

"""
This script changes the name of a State object in the
hbtn_0e_6_usa database
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

    #  Query the State objects with id = 2 and change its name to "New Mexico"
    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
    else:
        print("State with id 2 not found")

    #  free resources
    session.close()
