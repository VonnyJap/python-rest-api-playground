from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/customers/", response_model=list[schemas.CustomerRead])
def read_customers(db: Session = Depends(get_db)):
    return crud.get_customers(db)

@app.get("/customers/{customer_id}/orders", response_model=list[schemas.OrderRead])
def read_customer_orders(customer_id: int, db: Session = Depends(get_db)):
    orders = crud.get_orders_by_customer(db, customer_id)
    if orders is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return orders
