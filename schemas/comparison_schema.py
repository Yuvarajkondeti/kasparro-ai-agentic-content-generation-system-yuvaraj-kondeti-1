from pydantic import BaseModel
from typing import List

class ProductComparison(BaseModel):
    name: str
    ingredients: List[str]
    benefits: List[str]
    price: int

class ComparisonPage(BaseModel):
    product_a: ProductComparison
    product_b: ProductComparison