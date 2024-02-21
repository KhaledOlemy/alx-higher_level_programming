#!/usr/bin/python3
"""
fetch data of states table
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]))
    Base.metadata.createall(engine)
    mainSession = sessionmaker(bind=engine)
    session = mainSession()
    for ins in session.query(State).order_by(State.id):
        print("{}: {}".format(ins.id, ins.name))
