from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import random
import secrets
from pydantic import BaseModel
import time
import logging
import sys
from typing import Optional

import uuid

app = FastAPI()
security = HTTPBasic()


class Number(BaseModel):
    number: int = 0

class HTTPError(BaseModel):
    details: str

class Address(BaseModel):
    city: str = "undefined"
    street: str = "undefined"
    number: int = 0

class Struct(BaseModel):
    id: uuid.UUID
    name: str = "undefined"
    numbers: Optional[list[Number]] = [Number()]
    address: Address = Address()

def validate_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != "username" or credentials.password != "password":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return credentials.username


@app.get("/greet/{name}")
async def greet(name: str):
    return {'message': f"Hello {name}"}

@app.get("/random",
         responses={
             200: {"model": Number},
             400: {"model": HTTPError, 
                   "description": "raises an error if high is equal or smaller than low"},
             401: {"model": HTTPError,
                   "desciption": "raise an error if authnetication fails"}
         })
async def randomNumber(low: int, high: int, username = Depends(validate_credentials)):
    if high <= low:
        raise HTTPException(status_code=400, detail="Bad Request")
    return {'number': random.randint(low, high)}


@app.get("/struct")
async def struct(n: int = 1) -> list[Struct]:
    ret = []    
    for i in range(0, n):
        ret.append(Struct(id=uuid.uuid4()))
    return ret


@app.get("/sleep")
async def sleep(n: int = 10) -> Number:
    time.sleep(n)
    return Number(number=n)