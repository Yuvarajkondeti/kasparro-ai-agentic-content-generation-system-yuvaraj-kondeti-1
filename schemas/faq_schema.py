from pydantic import BaseModel
from typing import List

class FAQ(BaseModel):
    question: str
    answer: str
    category: str

class FAQPage(BaseModel):
    product_name: str
    faqs: List[FAQ]