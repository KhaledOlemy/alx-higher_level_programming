#!/usr/bin/python3
"""
insert
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
    new = State(name="Louisiana")
    session.add(new)
    session.commit()
    ins = session.query(State).filter(State.name == "Louisiana").first()
    print(ins.id)
