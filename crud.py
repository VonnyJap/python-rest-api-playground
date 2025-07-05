from sqlalchemy.orm import Session
from models import Customer

def get_customers(db: Session):
    return db.query(Customer).all()

def get_orders_by_customer(db: Session, customer_id: int):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    return customer.orders if customer else []