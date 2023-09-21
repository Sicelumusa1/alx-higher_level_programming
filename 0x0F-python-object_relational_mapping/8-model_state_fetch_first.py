#!/usr/bin/python3

"""
This script lists the first State objects from the hbtn_0e_6_usa database
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
    DATABASE_URI = (
        f'mysql://{username}:{password}@localhost:3360/{database_name}'
    )
    engine = create_engine(DATABASE_URI)

    #  Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    #  Query and print all state objects sorted by id
    state = session.query(State).order_by(State.id).first()

    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    #  free resources
    session.close()
