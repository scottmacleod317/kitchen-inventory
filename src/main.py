from typing import List

from fastapi import Depends, FastAPI, Response, status
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/products/", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)


@app.get("/product/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    return crud.get_product_by_id(db, product_id)


@app.post("/product/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)


@app.delete("/product/{product_id}", response_model=schemas.Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    crud.delete_product_by_id(db, product_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.patch("/product/{product_id}", response_model=schemas.Product)
def update_product(
    product_id: int, product_partial: schemas.ProductUpdate, db: Session = Depends(get_db)
):
    return crud.update_product_by_id(db, product_id, product_partial)
