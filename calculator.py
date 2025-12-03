import math

def scientific_calculator():
    print("=== Advanced Scientific Calculator ===")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Logarithm base 10 (log10)")
    print("8. Natural Logarithm (ln)")
    print("9. Sine (sin x)")
    print("10. Cosine (cos x)")
    print("11. Tangent (tan x)")
    print("12. Factorial (x!)")
    print("13. Absolute Value (|x|)")
    print("14. Exponential (e^x)")

    choice = input("Choose an operation (1-14): ")

    # Operations requiring two numbers
    if choice in ["1", "2", "3", "4", "5"]:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == "1":
            result = x + y
        elif choice == "2":
            result = x - y
        elif choice == "3":
            result = x * y
        elif choice == "4":
            if y == 0:
                return "Error: Division by zero"
            result = x / y
        elif choice == "5":
            result = math.pow(x, y)

    else:
        # Operations requiring one number
        x = float(input("Enter number: "))

        if choice == "6":
            if x < 0:
                return "Error: Negative value for square root"
            result = math.sqrt(x)

        elif choice == "7":
            if x <= 0:
                return "Error: log10 requires x > 0"
            result = math.log10(x)

        elif choice == "8":
            if x <= 0:
                return "Error: ln requires x > 0"
            result = math.log(x)

        elif choice == "9":
            result = math.sin(math.radians(x))

        elif choice == "10":
            result = math.cos(math.radians(x))

        elif choice == "11":
            result = math.tan(math.radians(x))

        elif choice == "12":
            if x < 0 or int(x) != x:
                return "Error: factorial requires non-negative integer"
            result = math.factorial(int(x))

        elif choice == "13":
            result = abs(x)

        elif choice == "14":
            result = math.exp(x)

        else:
            return "Invalid selection."

    return f"Result: {result}"


# Run calculator
print(scientific_calculator())

