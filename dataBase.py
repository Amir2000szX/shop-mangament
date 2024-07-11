from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, DateTime , text
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime,timezone
from persiantools.jdatetime import JalaliDateTime , JalaliDate
import pytz

iran_time = pytz.timezone('Iran')
DATABASE_URI = 'sqlite:///mydb.sqlite'
Base = declarative_base()
engine = create_engine(DATABASE_URI, echo=True)


class Sell(Base):
    __tablename__ = "sells"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nameOfGoods = Column(String(255))
    price = Column(DECIMAL(10, 0))
    color = Column(String(255))
    phone_num = Column(String(12))
    tags = Column(String(255))
    date = Column(DateTime(timezone=True))

    def __init__(self, nameOfGoods, price, date, tags, phone_num, color):
        self.nameOfGoods = nameOfGoods
        self.price = price
        self.date = date
        self.tags = tags
        self.phone_num = phone_num
        self.color = color

# Create all tables
Base.metadata.create_all(bind=engine)

# Session setup
Session = sessionmaker(bind=engine)
session = Session()

def add_row(name, price, tags, phone_num, color):
    today =JalaliDateTime.now(tz=iran_time)
    print(today.day)
    sell = Sell(name, price, datetime.now(), tags, phone_num, color)
    session.add(sell)
    session.commit()
def querry(command:str):
    with engine.connect() as connection:
        connection.execute(text(command))
        connection.commit()
def end():
    session.close()
today =JalaliDateTime.now(tz=iran_time)
print(today.year)

