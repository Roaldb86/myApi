from fastapi import FastAPI
import numpy as np

app = FastAPI()

products = [
    '7299234_F289',
    '7334587_F234',
    '7314258_F778',
    '7123453_F456',
    '7123565_F132'
]

@app.get("/")
async def recommendations():
    return {'hello'}

@app.get("/recommendations")
async def recommendations():
    results = {}
    for product in products:
        results[product] = np.random.randint(0, 10)
    return results


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
