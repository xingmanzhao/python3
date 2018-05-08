#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

__AUTHOR__ = 'xingman zhao'

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20),primary_key=True)
    name = Column(String(20))

engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/test')
DBSession = sessionmaker(bind=engine)

# session = DBSession()
# new_user = User(id='2',name='yangyu')
# session.add(new_user)
# session.commit()
# session.close()

def query():
    session_query = DBSession()
    user = session_query.query(User).filter(User.id == '2').all()
    if len(user) > 0:
        print('%s,%s' % (user[0].id,user[0].name))
    print(len(user))
    # print(user[0].id)
    session_query.close()

print(__name__)
if __name__ == '__main__':
    query()