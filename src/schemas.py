from typing import Union, Optional

from datetime import datetime
from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    quantity: float
    description: Union[str, None] = None
    category: str = "Misc"


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    quantity: Optional[float] = None
    description: Optional[str] = None
    category: Optional[str] = None


class Product(ProductBase):
    product_id: int
    time_created: datetime

    class Config:
        orm_mode = True
