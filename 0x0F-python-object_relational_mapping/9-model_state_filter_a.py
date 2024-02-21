#!/usr/bin/python3
"""
fetch states containing `a`
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
    ins = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id)
    for item in ins:
        print("{}: {}".format(item.id, item.name))
