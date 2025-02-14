from constants import MAX_VALUE, MIN_VALUE

def validate_number(value):
    """Validate if the number is within allowed range."""
    try:
        num = float(value)
        # Bug #1: Incorrect comparison (should be <= and >=)
        if num < MIN_VALUE or num > MAX_VALUE:
            raise ValueError(f"Value must be between {MIN_VALUE} and {MAX_VALUE}")
        return num
    except ValueError:
        raise ValueError("Invalid number format")

def format_result(result):
    """Format the result to specified decimal places."""
    # Bug #2: No import of DECIMAL_PLACES constant
    try:
        return round(result, DECIMAL_PLACES)
    except:
        return result  # Return unformatted in case of error