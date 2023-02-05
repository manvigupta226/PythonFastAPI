from database import Base
from sqlalchemy import Sring, Boolean, Integer, Coloumn,Text

class Item(Base):
    __tablename__= 'items'
    id=Column(Integer,primary_key= True)
    name=Coloumn(String(255), nullable=False,unique=True)
    description=Coloumn(Text)
    on_offer=Coloumn(Boolean, default=False)
