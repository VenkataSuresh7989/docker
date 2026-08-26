from app.models.user_model import User
from app.views.user_schema import UserCreate, UserUpdate
from fastapi import HTTPException
from sqlalchemy.orm import Session


# Create a new user
def create_user(db: Session, user: UserCreate):

  existing = db.query(User).filter(User.email == user.email).first()
  if existing:
    raise HTTPException(status_code=400, detail="Email already registered")

  db_user = User(name=user.name, email=user.email, gender=user.gender)
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user


# Fetch all users (READ)
def get_users(db: Session):

  return db.query(User).all()


# Update user by ID
def update_user(db: Session, user_id: int, user_data: UserUpdate):

  db_user = db.query(User).filter(User.id == user_id).first()
  if not db_user:
    raise HTTPException(status_code=404, detail="User not found")

  db_user.name = user_data.name
  db_user.email = user_data.email
  db_user.gender = user_data.gender

  db.commit()
  db.refresh(db_user)
  return db_user


# Delete user by ID
def delete_user(db: Session, user_id: int):

  db_user = db.query(User).filter(User.id == user_id).first()
  if not db_user:
    raise HTTPException(status_code=404, detail="User not found")

  db.delete(db_user)
  db.commit()
  return {"message": f"User with ID {user_id} deleted successfully"}