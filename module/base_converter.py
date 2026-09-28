"""base_converter.py - Base & ASCII Character Conversion Module
CSE1021 Algorithmic Toolkit"""

def decimal_to_base(n, base): #Converts a non-negative decimal integer n to string representation in given base (2 <= base <= 16)
    n, base = int(n), int(base)
    if n < 0:
        raise ValueError("Number must be non-negative.")
    if base < 2 or base > 16:
        raise ValueError("Base must be between 2 and 16.")
    if n == 0:
        return "0"
    digits = "0123456789ABCDEF"
    result = ""
    t = n
    while t > 0:
        remainder = t % base
        result = digits[remainder] + result
        t //= base
    return result

def base_to_decimal(s, base): #Converts a number string in given base (2 <= base <= 16) to decimal integer
    s, base = str(s), int(base)
    if base < 2 or base > 16:
        raise ValueError("Base must be between 2 and 16.")
    s = s.strip()
    s = s.upper()
    if not s:
        raise ValueError("Input string cannot be empty.")
    digits = "0123456789ABCDEF"
    decimal_val = 0
    for char in s:
        if char not in digits[:base]:
            raise ValueError(f"Invalid character '{char}' for base {base}.")
        decimal_val = decimal_val * base + digits.index(char)
    return decimal_val

def char_to_num(char): #Maps a single character to its ASCII integer value
    char=str(char)
    if len(char) != 1:
        raise ValueError("Input must be a single character.")
    return ord(char)

def num_to_char(val): #Maps an ASCII integer value back to its character representation
    val = int(val)
    if val < 0 or val > 127:
        raise ValueError("ASCII value must be between 0 and 127.")
    return chr(val)