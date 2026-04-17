import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent 
from langchain_core.tools import tool
from langchain_core.messages import SystemMessage
from tools import math_solver_logic,add_numbers,multiple_numbers,divide_numbers,square_of_numbers,whole_square_formula_add,whole_square_formula_subtract,difference_square_two_numbers

load_dotenv()


math_tools=[math_solver_logic,add_numbers,multiple_numbers,divide_numbers,square_of_numbers,whole_square_formula_add,whole_square_formula_subtract,difference_square_two_numbers]


# 2. Define the System Prompt (Your "Brain" Instructions)
SYSTEM_PROMPT = """You are 'Mathiest', a specialized AI math assistant. 
### TOOL HIERARCHY RULES:
1. **Priority 1 (Simple Math):** If the user asks for basic addition, subtraction, multiplication, or division, ALWAYS use the specific atomic tools (e.g., add_numbers, divide_numbers).
2. **Priority 2 (Algebraic Identities):** For whole squares or difference of squares, use the specific formula tools you have.
3. **Priority 3 (The Safety Net):** ONLY use 'math_solver_logic' (SymPy) if the problem involves variables (x, y), calculus, or complex symbolic simplification that the other tools cannot handle.
### RESPONSE STYLE:
- Explain your steps clearly using LaTeX formatting.
- If a tool returns an error, try an alternative tool or check your syntax."""

# 3. Initialize the Agent
llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)

# We pass the prompt directly as a string or SystemMessage
agent_executor = create_agent(
    model=llm, 
    tools=math_tools,
    system_prompt=SYSTEM_PROMPT
)

def run_mathiest(user_input: str):
    # Modern agents use message-based inputs
    response = agent_executor.invoke({
        "messages": [("user", user_input)]
    })
    return response["messages"][-1].content