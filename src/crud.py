from datetime import datetime, timezone

from sqlalchemy.orm import Session
from sqlalchemy import desc

from . import models, schemas


def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).order_by(desc("time_created")).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.ProductCreate):
    new_product = models.Product(time_created=datetime.now(tz=timezone.utc), **product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
