from fastapi import FastAPI, HTTPException, status, Response, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import moduls, schemas, utils
from .. database import get_db
from typing import List

router = APIRouter(
    prefix="/users",
    # tags= ['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserRes)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if db.query(moduls.Users).filter(moduls.Users.email == user.email).first():
        raise HTTPException(400, "This email is already exist")
    hash_pass = utils.get_password_hash(user.password)
    user.password = hash_pass
    new_user = moduls.Users(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user