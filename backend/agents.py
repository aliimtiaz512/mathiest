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
SYSTEM_PROMPT = """You are 'Mathiest', a professional AI Mathematician. 
Your primary goal is to provide precise, tool-verified solutions.

### TOOL SELECTION RULES:
1. **Atomic Math:** For basic arithmetic (addition, subtraction, multiplication, division), use the specific 'add_numbers', 'multiple_numbers', etc.
2. **Algebraic Identities:** If the problem matches (a+b)², (a-b)², or (a²-b²), use the 'whole_square_formula' tools.
3. **Complex/Symbolic Math:** For calculus (integration, derivatives), algebra (solving for x), or trigonometry, use 'math_solver_logic'. 
   - IMPORTANT: For SymPy, pass the expression in Python format (e.g., use 'x**2' for x²).

### OPERATIONAL GUIDELINES:
- **Never Guess:** If a calculation is required, you MUST use a tool. Do not solve it in your head.
- **Error Recovery:** If a tool returns an error, do not just apologize. Analyze the error, fix your input (e.g., check your syntax), and try the tool again.
- **Formatting:** Always present the final answer and major steps using LaTeX. 
- **Verbosely Accurate:** Explain the mathematical principle (like the Power Rule) ONLY after you have provided the tool-verified result.

### EXAMPLE FOR CALCULUS:
User: "Integrate x^2"
Action: Call math_solver_logic(query="integrate(x**2, x)")
"""

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