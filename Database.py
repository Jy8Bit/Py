from sqlalchemy import *;
from sqlalchemy.ext.declarative import declarative_base;
from sqlalchemy.orm import sessionmaker;

Base = declarative_base()

class Person(Base):
    __tablename__ = "User"
    
    mobile = Column("mobile", String, primary_key=True)
    firstName = Column("firstName", String)
    lastName = Column("lastName", String)
    Age = Column("Age", Integer)
    
    def __init__(self, mobile, firstName, lastName, Age):
        
        if not mobile.isdigit():
            raise ValueError("Mobile number must contain only digits")
        
        self.mobile = mobile
        self.firstName = firstName
        self.lastName = lastName
        self.Age = Age
        
    def __repr__(self):
        return f"({self.mobile}) {self.firstName} {self.lastName} {self.Age}"

class Wallet(Base):
    __tablename__ = "Wallet"
    
    walletID = Column("walletID", Integer, primary_key=True)
    owner = Column(String, ForeignKey("User.mobile"))
    balance = Column("balance", DECIMAL)
    crypto = Column("crypto", DECIMAL)
    
    def __init__(self, walletID, owner, balance, crypto):
        self.walletID = walletID
        self.owner = owner
        self.balance = balance
        self.crypto = crypto
        
    def __repr__(self):
        return f"({self.walletID}) Owner: {self.owner} Balance: {self.balance} {self.crypto}"
    
engine = create_engine("sqlite:///database.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person("09309212930", "Jay", "Mangas", 21)
session.add(person)
session.commit()

wallet = Wallet(1, person.mobile, 200000.50, 5)
session.add(wallet)
session.commit()