#!/usr/bin/python3
"""
fetch data of states table
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    mainSession = sessionmaker(bind=engine)
    session = mainSession()
    for ins in session.query(State).order_by(State.id):
        print("{}: {}".format(ins.id, ins.name))
