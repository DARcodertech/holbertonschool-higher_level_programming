#!/usr/bin/python3
"""
chang a state
"""

from sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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
    cities = (
            session.query(State.name, City.id, City.name)
            .join(City)
            .order_by(City.id)
            .all()
            )
    for state_name, city_id, city_name in cities:
        print(f"{state_name}: ({city_id}) {city_name}")
    session.close()
