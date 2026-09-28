"""factoring_engine.py 
Fundamental factoring algorithms for CSE1021:
1. Euclidean GCD
2. Smallest Divisor
3. Prime Factorization
4. Sieve Prime Generation
5. Integer Square Root Approximation

No external libraries are required"""

def GCD_euclid(a,b): #Return the greatest common divisor (GCD) of two integers using the Euclidean algorithm
    a = int(a)
    b = int(b)
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def smallest_divisor(n): #Return the smallest divisor of n greater than 1. If n is prime, n itself is returned
    n = int(n)
    if n < 2:
        raise ValueError("n must be at least 2")   
    if n % 2 == 0:
        return 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2
    return n

def prime_factors(n): #Return the prime factorization of n as a list.
    n=int(n)
    if n < 2:
        raise ValueError("n must be at least 2")
    f = []
    while n > 1:
        d = smallest_divisor(n)
        f.append(d)
        n //= d
    return f

def generate_primes(l): #Generate all prime numbers less than or equal to limit using the Sieve of Eratosthenes
    l=int(l)
    if l < 2:
        return []
    is_prime = [True] * (l + 1)
    is_prime[0] = False
    is_prime[1] = False
    n = 2
    while n * n <= l:
        if is_prime[n]:
            m = n * n
            while m <= l:
                is_prime[m] = False
                m += n
        n += 1
    p = []
    for n in range(2, l + 1):
        if is_prime[n]:
            p.append(n)
    return p

def integer_square_root(n): #Return the integer square root of n. if perfect root dont exist, it return 2 digit after decimal
    n=int(n)
    if n < 0:
        raise ValueError("n must be non-negative")
    r = n**0.5
    return round(r,2)
