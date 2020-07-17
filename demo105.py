from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine1 = create_engine('sqlite:///data/demo105.sqlite.db', echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    dept = Column(String)
    addr = Column(String)

    def __repr__(self):
        return f"<User name:{self.name}, age:{self.age}, department:{self.dept}, address:{self.addr}>"


print(User.__tablename__, User.__table__)
Base.metadata.create_all(engine1)

sqlite_session = sessionmaker(bind=engine1)
session1 = sqlite_session()
user1 = User(name='Mark', age=43, dept='RD', addr='Taipei')
user2 = User(name='James', age=38, dept='FAE', addr='Hsinchu')
session1.add(user1)
session1.add(user2)

session1.commit()
session2 = sqlite_session()
all_users = session2.query(User)
for u in all_users:
    print(u)
session2.commit()
