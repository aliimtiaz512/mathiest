from fastapi import FastAPI
from pydantic import BaseModel
from agents import run_mathiest

app = FastAPI()

class MathRequest(BaseModel):
    problem: str

@app.get("/")
def home():
    return {"message": "Mathiest API is running!"}

@app.post("/solve")
async def solve_math(request: MathRequest):
    # This is where we will call our LangChain Agent later
    answer=run_mathiest(request.problem)
    return {"answer": answer}