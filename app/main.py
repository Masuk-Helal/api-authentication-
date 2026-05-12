from fastapi import FastAPI, status, Depends, HTTPException
from sqlalchemy.orm import Session
from . database import get_db, engine
from . import schemas
from . import moduls

app = FastAPI()

moduls.Base.metadata.create_all(bind=engine)


# User Endpoints
@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserRes)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = moduls.Users(**user.model_dump())
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
    
    
    # if db_user:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    
    # new_user = moduls.Usersa(email=user.email, password=user.password)


@app.get("/users", response_model=list[schemas.UserRes])
def get_users(db: Session = Depends(get_db)):
    return db.query(moduls.Usersa).all()


@app.get("/users/{user_id}", response_model=schemas.UserRes)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(moduls.Usersa).filter(moduls.Usersa.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# FoodItem Endpoints
@app.post("/fooditems", response_model=schemas.FoodItemRes)
def create_food_item(food: schemas.FoodItemCreate, db: Session = Depends(get_db)):
    new_food = moduls.FoodItem(name=food.name, price=food.price, image=food.image)
    db.add(new_food)
    db.commit()
    db.refresh(new_food)
    return new_food


@app.get("/fooditems", response_model=list[schemas.FoodItemRes])
def get_food_items(db: Session = Depends(get_db)):
    return db.query(moduls.FoodItem).all()

