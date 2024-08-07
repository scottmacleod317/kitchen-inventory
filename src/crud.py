from datetime import datetime, timezone

from fastapi import HTTPException

from sqlalchemy.orm import Session
from sqlalchemy import desc

from . import models, schemas


def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).order_by(desc("time_created")).offset(skip).limit(limit).all()


def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.product_id == product_id).first()


def create_product(db: Session, product: schemas.ProductCreate):
    new_product = models.Product(time_created=datetime.now(tz=timezone.utc), **product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def delete_product_by_id(db: Session, product_id: int):
    product = db.query(models.Product).filter(models.Product.product_id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Product not found with ID {product_id}")
