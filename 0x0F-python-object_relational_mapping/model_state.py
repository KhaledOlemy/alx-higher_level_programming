#!/usr/bin/python3
"""
State class, Base using declarative_base
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

meta = MetaData()
Base = declarative_base(metadata=meta)


class State(Base):
    """
    State class; id, name
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
