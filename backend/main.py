from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents import run_mathiest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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