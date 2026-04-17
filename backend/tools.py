import math
from sympy import sympify
from langchain_core.tools import tool

@tool
def math_solver_logic(query: str):
    """
    Solves complex math like algebra, calculus (integrals/derivatives), 
    and equation solving. Use this ONLY if basic tools cannot solve the problem.
    """
    print(">>> AGENT IS USING: math_solver_logic")
    try:
        result = sympify(query)
        return str(result)
    except Exception as e:
        return f"Error: {e}"
    
@tool    
def add_numbers(numbers:list[int]):
    """
    Use this for sum of numbers.
    """
    print(">>> AGENT IS USING: add_numbers")
    try:
        total=sum(numbers)
        return total
    except Exception as e:
        return f"Error: {e}"
    
@tool    
def multiple_numbers(numbers:list[int]):
    """
    Use this for multiple numbers.
    """
    print(">>> AGENT IS USING: multiple_numbers")
    try:
        total=math.prod(numbers)
        return total
    except Exception as e:
        return f"Error: {e}"
    
@tool    
def divide_numbers(divident:int,divisor=int):
    "Use this to divide two numbers"
    print(">>> AGENT IS USING: divide_numbers")
    try:
        if divisor==0:
            return "This is not possible in mathematics."
        else:
            total=divident/divisor
            return total
    except Exception as e:
        return f"Error: {e}"
    
@tool    
def square_of_numbers(numbers:list[int]):
    """Use for taking square of numbers"""
    print(">>> AGENT IS USING: square_of_numbers")
    try:
        square=[]
        for i in range(len(numbers-1)):
            result=i*i
            square.append(result)
        return square
    except Exception as e:
        return f"Error {e}"
    
@tool    
def whole_square_formula_add(a:int, b:int):
    """Use for (a+b)^2"""
    print(">>> AGENT IS USING: whole_square_formula_add")
    try:
        total=a+b+2*a*b
        return total
    except Exception as e:
        return f"Error {e}"

@tool        
def whole_square_formula_subtract(a:int, b:int):
    """Use for (a-b)^2"""
    print(">>> AGENT IS USING: whole_square_formula_subtract")
    try:
        total=a+b-2*a*b
        return total
    except Exception as e:
        return f"Error {e}"

@tool
def difference_square_two_numbers(a:int, b:int):
   """Use for (a^2-b^2)"""
   print(">>> AGENT IS USING: difference_square_two_numbers")
   try:
       total=(a+b)*(a-b)
       return total
   except Exception as e:
        return f"Error {e}"
     
