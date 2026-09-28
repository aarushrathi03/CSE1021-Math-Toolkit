# =========================================================
# Student Name : [Aarush Rathi]
# Reg Number : [26BEC10121]
# Course Code : CSE1021 - Introduction to Problem Solving
# Slot : [A11+A12+A13+A14+D11+D12]
# Project : Algorithmic Mathematical &amp; Number Theory Toolkit
# =========================================================

import sys
import datetime

from module.factoring_engine import (GCD_euclid, prime_factors, smallest_divisor, generate_primes, integer_square_root)

from module.sequence_analytics import (fibonacci_sequence, nth_fibonacci, power_modulo, pseudo_random_gen)

from module.array_processor import (reverse_array, remove_duplicates, partition_array, kth_smallest_element)

from module.base_converter import (decimal_to_base, base_to_decimal, char_to_num, num_to_char)

from module.validator_utils import (validate_integer, validate_integer_list)

from module.logger_service import (log_operation, read_logs)

def show_banner():
    print("=" * 60)
    print(" CSE1021: ALGORITHMIC MATHEMATICAL & ARRAY TOOLKIT")
    print(" Developed by: Aarush Rathi (26BEC10121)")
    print(" This toolkit provides various mathematical, number theory, and array operations.")
    print(f" Session Started: " f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}") 
    print("=" * 60)

def menu_factoring():
    print("\n--- Factoring & Prime Mathematics ---")
    print("1. Euclidean GCD")
    print("2. Prime Factors Decomposition")
    print("3. Smallest Prime Divisor")
    print("4. Generate Prime Numbers (Sieve)")
    print("5. Integer Square Root Approximation")
    print("0. Back to Main Menu")
    
    choice = input("Select option (0-5): ").strip()
    
    if choice == "1":
        valid_a, a, msg_a = validate_integer(input("Enter first integer (a): "))
        valid_b, b, msg_b = validate_integer(input("Enter second integer (b): "))
        if not valid_a:
            print(f"Error: {msg_a}")
            return
        if not valid_b:
            print(f"Error: {msg_b}")
            return           
        res = GCD_euclid(a, b) # If your function in factoring_engine is GCD_euclid, keep GCD_euclid(a, b)
        print(f"-> GCD({a}, {b}) = {res}")
        log_operation("GCD", f"a={a}, b={b}, result={res}")
        
    elif choice == "2":
        valid, n, msg = validate_integer(input("Enter positive integer (n): "), min_val=2)
        if not valid:
            print(f"Error: {msg}")
            return           
        res = prime_factors(n)
        print(f"-> Prime Factors of {n}: {res}")
        log_operation("PRIME_FACTORS", f"n={n}, result={res}")
        
    elif choice == "3":
        valid, n, msg = validate_integer(input("Enter integer greater than 1: "), min_val=2)
        if not valid:
            print(f"Error: {msg}")
            return            
        res = smallest_divisor(n)
        print(f"-> Smallest Divisor of {n}: {res}")
        log_operation("SMALLEST_DIVISOR", f"n={n}, result={res}")
        
    elif choice == "4":
        valid, limit, msg = validate_integer(input("Enter upper limit for primes: "), min_val=2)
        if not valid:
            print(f"Error: {msg}")
            return           
        res = generate_primes(limit)
        print(f"-> Primes up to {limit}: {res}")
        log_operation("GENERATE_PRIMES", f"limit={limit}, count={len(res)}")
        
    elif choice == "5":
        valid, n, msg = validate_integer(input("Enter non-negative integer: "), min_val=0)
        if not valid:
            print(f"Error: {msg}")
            return
        res = integer_square_root(n)
        print(f"-> Integer Square Root of {n}: {res}")
        log_operation("SQUARE_ROOT", f"n={n}, result={res}")

    elif choice == "0":
        return
    
    else:
        print("Invalid choice!")

           
def menu_sequences():
    print("\n--- Sequences & Number Theory Analytics ---")
    print("1. Fibonacci Sequence Generator")
    print("2. Find Nth Fibonacci Number")
    print("3. Modular Exponentiation (base^exp % mod)")
    print("4. Pseudo-Random Number Generator (LCG)")
    print("0. Back to Main Menu")
    
    choice = input("Select option (0-4): ").strip()
    
    if choice == "1":
        valid, terms, msg = validate_integer(input("Enter number of terms: "), min_val=1)
        if not valid:
            print(f"Error: {msg}")
            return           
        res = fibonacci_sequence(terms)
        print(f"-> Fibonacci ({terms} terms): {res}")
        log_operation("FIBONACCI_SEQ", f"terms={terms}, result={res}")
        
    elif choice == "2":
        valid, n, msg = validate_integer(input("Enter term index n (0-based): "), min_val=0)
        if not valid:
            print(f"Error: {msg}")
            return         
        res = nth_fibonacci(n)
        print(f"-> {n}-th Fibonacci Number: {res}")
        log_operation("NTH_FIBONACCI", f"n={n}, result={res}")
        
    elif choice == "3":
        valid_b, base, msg_b = validate_integer(input("Enter base: "))
        if not valid_b:
            print(f"Error: {msg_b}")
            return         
        valid_e, exp, msg_e = validate_integer(input("Enter exponent: "), min_val=0)
        if not valid_e:
            print(f"Error: {msg_e}")
            return        
        valid_m, mod, msg_m = validate_integer(input("Enter modulus (>0): "), min_val=1)
        if not valid_m:
            print(f"Error: {msg_m}")
            return        
        res = power_modulo(base, exp, mod)
        print(f"-> ({base}^{exp}) % {mod} = {res}")
        log_operation("MODULAR_EXP", f"base={base}, exp={exp}, mod={mod}, result={res}")
        
    elif choice == "4":
        valid_s, seed, msg_s = validate_integer(input("Enter seed value: "))
        if not valid_s:
            print(f"Error: {msg_s}")
            return       
        valid_c, count, msg_c = validate_integer(input("Enter count of numbers: "), min_val=1)
        if not valid_c:
            print(f"Error: {msg_c}")
            return  
        res = pseudo_random_gen(seed, count, 1, 100)
        print(f"-> Generated Pseudo-Random List (1-100): {res}")
        log_operation("PSEUDO_RANDOM", f"seed={seed}, count={count}, result={res}")

    elif choice == "0":
        return
    
    else:
        print("Invalid choice!")

def menu_arrays():
    print("\n--- Computational Array Operations ---")
    print("1. Reverse Array Order")
    print("2. Remove Duplicates")
    print("3. Partition Array around Pivot")
    print("4. Find Kth Smallest Element")
    print("0. Back to Main Menu")
    
    choice = input("Select option (0-4): ").strip()
    
    if choice in ("1", "2", "3", "4"):
        raw_input = input("Enter array elements (separated by space or comma): ")
        valid, arr, msg = validate_integer_list(raw_input)
        if not valid:
            print(f"Error: {msg}")
            return
   
        if choice == "1":
            res = reverse_array(arr)
            print(f"-> Original: {arr}")
            print(f"-> Reversed: {res}")
            log_operation("REVERSE_ARRAY", f"original={arr}, result={res}")
            
        elif choice == "2":
            res = remove_duplicates(arr)
            print(f"-> Unique Array: {res}")
            log_operation("REMOVE_DUPLICATES", f"result={res}")
            
        elif choice == "3":
            valid_p, pivot, msg_p = validate_integer(input("Enter pivot integer: "))
            if not valid_p:
                print(f"Error: {msg_p}")
                return    
            less, equal, greater = partition_array(arr, pivot)
            print(f"-> Less than {pivot}: {less}")
            print(f"-> Equal to {pivot}: {equal}")
            print(f"-> Greater than {pivot}: {greater}")
            log_operation("PARTITION_ARRAY", f"pivot={pivot}, less={less}, equal={equal}, greater={greater}")
            
        elif choice == "4":
            valid_k, k, msg_k = validate_integer(input(f"Enter k (1 to {len(arr)}): "), min_val=1, max_val=len(arr))
            if not valid_k:
                print(f"Error: {msg_k}")
                return     
            res = kth_smallest_element(arr, k)
            print(f"-> {k}-th Smallest Element: {res}")
            log_operation("KTH_SMALLEST", f"k={k}, result={res}")

        elif choice == "0":
            return

        else:
            print("Invalid choice!")

def menu_base_conversions():
    print("\n--- Base & Character Conversions ---")
    print("1. Decimal to Base (Binary/Octal/Hex/Custom)")
    print("2. Base to Decimal")
    print("3. Character to ASCII Number")
    print("4. ASCII Number to Character")
    print("0. Back to Main Menu")
    
    choice = input("Select option (0-4): ").strip()
    
    if choice == "1":
        valid_n, n, msg_n = validate_integer(input("Enter non-negative integer: "), min_val=0)
        if not valid_n:
            print(f"Error: {msg_n}")
            return  
        valid_b, base, msg_b = validate_integer(input("Enter base (2-16): "), min_val=2, max_val=16)
        if not valid_b:
            print(f"Error: {msg_b}")
            return  
        res = decimal_to_base(n, base)
        print(f"-> Decimal {n} in Base {base}: {res}")
        log_operation("DECIMAL_TO_BASE", f"n={n}, base={base}, result={res}")
        
    elif choice == "2":
        s = input("Enter number string: ").strip()
        valid_b, base, msg_b = validate_integer(input("Enter base (2-16): "), min_val=2, max_val=16)
        if not valid_b:
            print(f"Error: {msg_b}")
            return  
        try:
            res = base_to_decimal(s, base)
            print(f"-> Base {base} '{s}' in Decimal: {res}")
            log_operation("BASE_TO_DECIMAL", f"s={s}, base={base}, result={res}")
        except ValueError as e:
            print(f"Error: {e}")
            
    elif choice == "3":
        char = input("Enter a single character: ")
        if len(char) == 1:
            res = char_to_num(char)
            print(f"-> ASCII value of '{char}': {res}")
            log_operation("CHAR_TO_NUM", f"char={char}, ascii={res}")
        else:
            print("Error: Input must be exactly 1 character.")
            
    elif choice == "4":
        valid_v, val, msg_v = validate_integer(input("Enter ASCII code (0-127): "), min_val=0, max_val=127)
        if not valid_v:
            print(f"Error: {msg_v}")
            return  
        res = num_to_char(val)
        print(f"-> Character for ASCII {val}: '{res}'")
        log_operation("NUM_TO_CHAR", f"ascii={val}, char={res}")

    elif choice == "0":
        return

    else:
        print("Invalid choice!")

def main():
    show_banner()
    log_operation("SYSTEM","Toolkit CLI session launched")
    while True:
        print("\n================ MAIN MENU ================")
        print("1. Factoring & Prime Mathematics")
        print("2. Sequences & Number Theory Analytics")
        print("3. Computational Array Operations")
        print("4. Base & Character Conversions")
        print("5. View Execution Logs")
        print("6. About Developer & Project Info")
        print("0. Exit Toolkit")
        print("===========================================")

        choice = input("Enter choice (0-6): ").strip()

        if choice == "1":
            menu_factoring()

        elif choice == "2":
            menu_sequences()

        elif choice == "3":
            menu_arrays()

        elif choice == "4":
            menu_base_conversions()

        elif choice == "5":
            print("\n--- Recent Log History (`execution.log`) ---")
            logs = read_logs("execution.log")
            for line in logs[-10:]:
                print(line, end="")

        elif choice == "6":
            print("\n--- Project &amp; Developer Metadata ---")
            print("Project: Algorithmic Mathematical & Number Theory Toolkit")
            print("Developer: Aarush Rathi (26BEC10121)")
            print("Description: This toolkit provides various mathematical, number theory, and array operations.")
            print("Architecture : 10 Modular Files (CLI)")

        elif choice == "0":
            print("\nExiting Algorithmic Toolkit. Goodbye!")
            log_operation("SYSTEM","Toolkit CLI session terminated")
            sys.exit(0)

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()