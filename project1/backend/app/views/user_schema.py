from typing import Literal
from pydantic import BaseModel, EmailStr


# Base schema for shared attributes
class UserBase(BaseModel):

  name: str
  email: str
  gender: Literal["Male", "Female", "Others"]


# Schema for creating a user
class UserCreate(UserBase):

  pass


# Schema for updating a user
class UserUpdate(UserBase):

  pass


# Schema for returning user response (includes ID)
class UserResponse(UserBase):

  id: int

  class Config:

    from_attributes = True