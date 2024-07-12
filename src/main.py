from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import random
import json

app = FastAPI()

class Quote(BaseModel):
    id: int
    author: str
    frase: str

class QuoteResponse(BaseModel):
    author: str
    frase: str

@app.get("/", response_model=QuoteResponse)
def get_random_quote():
    with open("equilibra.json") as file:
        quotes_list = json.load(file)
        quote = random.choice(quotes_list)
        return QuoteResponse(author=quote["author"], frase=quote["frase"])
