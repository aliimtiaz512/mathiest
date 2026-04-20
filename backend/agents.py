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

### FORMATTING RULES (STRICT):
1. NEVER use double dollar signs ($$). 
2. Use plain text for formulas so they are easy to read in a terminal.
3. Use '*' for multiplication and '^' for powers.
4. Use Markdown bullet points for steps.

### MANDATORY RESPONSE STRUCTURE:
You must provide all three parts in order:
1. Formula: Clearly state the rule being used (e.g., a^2 - b^2 = (a-b)(a+b)).
2. Tool Result: State the number returned by the tool.
3. The Logic: Show the manual calculation steps (e.g., 10-4 = 6, 10+4 = 14, 6*14 = 84).

### EXAMPLE:
Formula: a^2 - b^2 = (a-b)(a+b)
Tool Result: 84
Logic: 
- Substituting values: (10-4) * (10+4)
- Intermediate steps: 6 * 14
- Final Result: 84
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