from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# A Pydantic model for validating request data
class FibonacciRequest(BaseModel):
    terms: int

def generate_fibonacci(n: int):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fibonacci_series = [0, 1]
    for i in range(2, n):
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
    return fibonacci_series

@app.get("/")   
def read_root():
    return {"message": "Hello, Interns!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/square/{number}")
def square(number: int):
    return {"message": f"Hello, {number * number}!"}

@app.post("/fibonacci/")
def calculate_fibonacci(request: FibonacciRequest):
    series = generate_fibonacci(request.terms)
    return {"fibonacci_series": series}


