"""validator_utils.py - Input Validation & Error Handling Module
CSE1021 Algorithmic Toolkit"""

def validate_integer( input_str, min_val=None, max_val=None): #Validates if input string is a valid integer within optional bounds
    input_str, min_val, max_val = str(input_str), int(min_val) if min_val is not None else None, int(max_val) if max_val is not None else None
    try:
        val = int(input_str.strip())
        if min_val is not None and val < min_val:
            return False, val, f"Value must be at least {min_val}."
        if max_val is not None and val > max_val:
            return False, val, f"Value must be at most {max_val}."
        return True, val, "Valid input."
    except ValueError:
        return False, 0, "Invalid input! Please enter a whole integer number."

def validate_integer_list( input_str ): #Parses space-separated or comma-separated string into a list of integers
    input_str = str(input_str).strip()
    r = input_str.replace(",", " ").split()
    if not r:
        return False, [], "Input list cannot be empty."
    p = []
    for item in r:
        try:
            p.append(int(item))
        except ValueError:
            return (False, [], f"Invalid element '{item}'. All items must be integers.")
    return True, p, "Valid array input."