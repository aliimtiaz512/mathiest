import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent 
from langchain_core.tools import Tool
from langchain_core.messages import SystemMessage
from sympy import sympify

load_dotenv()

# 1. Define Tool Logic
def math_solver_logic(query: str):
    try:
        result = sympify(query)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

math_tool = Tool(
    name="Math_Calculator",
    func=math_solver_logic,
    description="Solve complex math, algebra, and calculus equations."
)

# 2. Define the System Prompt (Your "Brain" Instructions)
SYSTEM_PROMPT = """You are 'Mathiest', a specialized AI math assistant. 
Your goal is to provide 100% accurate mathematical solutions.
When a user asks a math question:
1. Use the Math_Calculator tool for any calculation or simplification.
2. Explain your steps clearly using LaTeX formatting.
3. If the tool returns an error, double-check the syntax and try again."""

# 3. Initialize the Agent
llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)

# We pass the prompt directly as a string or SystemMessage
agent_executor = create_agent(
    model=llm, 
    tools=[math_tool],
    system_prompt=SYSTEM_PROMPT
)

def run_mathiest(user_input: str):
    # Modern agents use message-based inputs
    response = agent_executor.invoke({
        "messages": [("user", user_input)]
    })
    return response["messages"][-1].content