from sqlalchemy import Column, DateTime, Integer, String, Float

from .database import Base


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    time_created = Column(DateTime, index=True, nullable=False)
    name = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    description = Column(String(30), nullable=True)
    category = Column(String(30), nullable=True)
