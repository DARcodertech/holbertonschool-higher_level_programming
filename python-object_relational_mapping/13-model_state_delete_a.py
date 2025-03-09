#!/usr/bin/python3
"""
chang a state
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
    try:
        states_to_delete = session.query(State).filter(
            State.name.like('%a%')
        ).all()
    for state in states_to_delete:
        session.delete(state)
        session.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()
