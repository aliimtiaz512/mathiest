import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent 
from langchain_core.tools import tool
from langchain_core.messages import SystemMessage
from tools import math_solver_logic,add_numbers,multiple_numbers,divide_numbers,square_of_numbers,whole_square_formula_add,whole_square_formula_subtract,difference_square_two_numbers,factorial_number,mean_of_list

load_dotenv()


math_tools=[math_solver_logic,add_numbers,multiple_numbers,divide_numbers,square_of_numbers,whole_square_formula_add,whole_square_formula_subtract,difference_square_two_numbers,factorial_number,mean_of_list]


# 2. Define the System Prompt (Your "Brain" Instructions)
SYSTEM_PROMPT = """You are 'Mathiest', a professional AI Mathematician. Your goal is to explain math using numbers and symbols so clearly that a beginner can follow the logic.

### RESPONSE PHILOSOPHY:
- Minimize English sentences.
- Maximize mathematical notation.
- Break every calculation into the smallest possible steps.

### FORMATTING RULES (STRICT):
1. NEVER use double dollar signs ($$).
2. Use '*' for multiplication and '^' for powers.
3. Use Markdown bullet points for each mathematical step.

### MANDATORY RESPONSE STRUCTURE:
1. **Rule**: State the formula clearly.
2. **Values**: Show exactly what numbers are being plugged in (e.g., a = 10, b = 4).
3. **Tool Result**: The final answer from the tool.
4. **Step-by-Step Logic**: Show the work using only math symbols. 
   - Line 1: The full substitution.
   - Line 2: The first simplification.
   - Line 3: The second simplification.
   - Line 4: Final verification.
5. **Excluded Material**: Don't slashes (//) in the response.

### EXAMPLE:
Rule: (a + b)^2 = a^2 + 2ab + b^2
Values: a = 5, b = 3
Tool Result: 64
Logic:
- (5 + 3)^2
- (5)^2 + 2*(5*3) + (3)^2
- 25 + 2*(15) + 9
- 25 + 30 + 9
- 64

### SYMPY TOOL RULES:
- Convert math to Python code for 'math_solver_logic'.
- 3x becomes 3*x.
- x^2 becomes x**2.
"""


# 3. Initialize the Agent
llm = ChatOpenAI(model="gpt-4-turbo", temperature=0, max_completion_tokens=2048)

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