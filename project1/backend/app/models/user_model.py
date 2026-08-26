from app.config.database import Base
from sqlalchemy import Column, Enum, Integer, String


class User(Base):

  __tablename__ = "userinfo"

  # Auto-incrementing Primary Key
  id = Column(Integer, primary_key=True, index=True, autoincrement=True)

  # User details
  name = Column(String(100), nullable=False)
  email = Column(String(100), unique=True, nullable=False, index=True)

  # Enum restricting values to Male, Female, Others
  gender = Column(Enum("Male", "Female", "Others"), nullable=False)