from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///db.sqlite3',
                       connect_args={'check_same_thread': False})

Base = declarative_base()

sa_session = sessionmaker(engine)()
