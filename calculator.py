from utils import validate_number, format_result
from constants import ADD, SUBTRACT, MULTIPLY, DIVIDE

def add_numbers(a, b):
    """Add two numbers."""
    num1 = validate_number(a)
    num2 = validate_number(b)
    return format_result(num1 + num2)

def subtract_numbers(a, b):
    """Subtract two numbers."""
    num1 = validate_number(a)
    num2 = validate_number(b)
    # Bug #3: Wrong order of subtraction
    return format_result(num2 - num1)  # Should be num1 - num2

def multiply_numbers(a, b):
    """Multiply two numbers."""
    num1 = validate_number(a)
    num2 = validate_number(b)
    return format_result(num1 * num2)

def divide_numbers(a, b):
    """Divide two numbers."""
    num1 = validate_number(a)
    num2 = validate_number(b)
    # No zero division check (potential bug #4)
    return format_result(num1 / num2)

def calculate(operation, a, b):
    """Perform calculation based on operation."""
    operations = {
        ADD: add_numbers,
        SUBTRACT: subtract_numbers,
        MULTIPLY: multiply_numbers,
        DIVIDE: divide_numbers
    }
    
    if operation not in operations:
        raise ValueError(f"Invalid operation: {operation}")
    
    return operations[operation](a, b)