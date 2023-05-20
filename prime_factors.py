'''Algorithm for returning the prime factors of a number n.
    Contains a function for computing Euler's totient function as well'''

from math import sqrt

def prime_factors(n):
    '''Input a number n. Output is a list of prime factors.'''
    p_factors = []
    if n % 2 == 0:
        p_factors.append(2)
        while n % 2 == 0:
            n /= 2
            
    factor = 3
    max_factor = sqrt(n)
    
    while n > 1 and factor <= max_factor:
        if n % factor == 0:
            p_factors.append(factor)
            while n % factor == 0:
                n /= factor
            max_factor = sqrt(n)
        factor += 2
    if n != 1:
        p_factors.append(n)
        
    return p_factors
    
def totient(n, prime_facts = None):
    '''Euler's totient function, phi(n), counts the numbers less than n
    that are coprime with n. Input an integer. Optionally input list
    of prime factors to avoid double work.'''
    result = n
    if not prime_facts:
        prime_facts = prime_factors(n)
    for prime in prime_facts:
        result *= (prime-1)
        result /= prime
    return result

    
def main():
    '''Asks for a number as input and displays the list of prime factors
    as well as the totient of the number.'''
    print("Returns list of prime factors and phi(n).")
    user_input = int(input("Input number: "))
    result = prime_factors(user_input)
    print(result)
    print("Totient: %d" % totient(user_input, result))
    
if __name__ == '__main__':
    main()
    
