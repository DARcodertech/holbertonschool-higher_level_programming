#!/usr/bin/python3
"""
list a state
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    states_with_a = (
                    session.query(State)
                    .filter(State.name.like('%a%'))
                    .order_by(State.id)
                    .all()
                    )
    for state in states_with_a:
        print(f"{state.id}: {state.name}")
    session.close()
