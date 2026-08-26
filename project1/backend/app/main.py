import time
from app.config.database import Base, engine, get_db
from app.controllers import user_controller
from app.views.user_schema import UserCreate, UserResponse, UserUpdate
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

# Wait for MySQL database container to start
max_retries = 10
for i in range(max_retries):
  try:
    Base.metadata.create_all(bind=engine)
    print("Database connected and tables created!")
    break
  except OperationalError as e:
    if i == max_retries - 1:
      print("Could not connect to MySQL database.")
      raise e
    print(f"Waiting for database... retry {i+1}/{max_retries}")
    time.sleep(3)

app = FastAPI(title="Vue FastAPI CRUD")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/users", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
  return user_controller.create_user(db, user)


@app.get("/users", response_model=list[UserResponse])
def read_all(db: Session = Depends(get_db)):
  return user_controller.get_users(db)


@app.put("/users/{user_id}", response_model=UserResponse)
def update(
    user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)
):
  return user_controller.update_user(db, user_id, user_data)


@app.delete("/users/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
  return user_controller.delete_user(db, user_id)