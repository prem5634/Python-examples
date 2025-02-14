from calculator import calculate
from constants import ADD, SUBTRACT, MULTIPLY, DIVIDE

def main():
    """Main function to demonstrate calculator operations."""
    try:
        # Example calculations
        print("Calculator Demo")
        print("-" * 20)
        
        # Addition
        result = calculate(ADD, 10, 5)
        print(f"10 + 5 = {result}")
        
        # Subtraction (will show wrong result due to bug)
        result = calculate(SUBTRACT, 10, 5)
        print(f"10 - 5 = {result}")
        
        # Multiplication
        result = calculate(MULTIPLY, 10, 5)
        print(f"10 * 5 = {result}")
        
        # Division (potential division by zero error)
        result = calculate(DIVIDE, 10, 0)
        print(f"10 / 0 = {result}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()