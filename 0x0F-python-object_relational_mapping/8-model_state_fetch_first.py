#!/usr/bin/python3
"""
fetch first state
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    mainSession = sessionmaker(bind=engine)
    session = mainSession()
    ins = session.query(State).order_by(State.id).first()
    if ins:
        print("{}: {}".format(ins.id, ins.name))
    else:
        print("Nothing")
