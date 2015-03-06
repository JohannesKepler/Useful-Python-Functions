from math import sqrt

def prime_factors(n):
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
    
def main():
    print "Returns list of prime factors."
    user_input = int(raw_input("Input number: "))
    print prime_factors(user_input)
    
if __name__ == '__main__':
    main()
    
