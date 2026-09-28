"""sequence_analytics.py - Sequences &amp; Number Theory Module CSE1021 Algorithmic Toolkit"""

def fibonacci_sequence(t): #Generates Fibonacci sequence up to specified number of terms
    t=int(t)
    if t <= 0:
        return []
    if t == 1:
        return [0]
    seq = [0, 1]
    for i in range(2, t):
        seq.append(seq[-1] + seq[-2])
    return seq

def nth_fibonacci(n): #Finds the Nth Fibonacci number iteratively
    n=int(n)
    if n < 0:
        raise ValueError("Index cannot be negative.")
    if n == 0 or n == 1:
        return n
    pv, cv = 0, 1
    for i in range(2, n + 1):
        pv, cv = cv, pv + cv
    return cv

def power_modulo(base, exp, mod): #Calculates (base^exp) % mod using binary exponentiation algorithm
    base, exp, mod = int(base), int(exp), int(mod)
    if mod <= 0:
        raise ValueError("Modulus must be positive.")
    r = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            r = (r * base) % mod
        exp //= 2
        base = (base * base) % mod
    return r

def pseudo_random_gen(seed, count, min_val, max_val): #Linear Congruential Generator (LCG) for pseudo-random numbers
    if count <= 0 or min_val >= max_val:
        return []
    a = 1664525
    c = 1013904223
    m = 2**32
    generated_nums = []
    current_val = seed
    for i in range(count):
        current_val = (a * current_val + c) % m
        scaled = min_val + (current_val % (max_val - min_val + 1))
        generated_nums.append(scaled)
    return generated_nums