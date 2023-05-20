def prime_sieve(limit):
    # Initialize the primality list
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            # Mark factors non-prime
            for n in range(i, limit, i):
                a[n] = False
                
def composite_sieve(limit):
    # Initialize the primality list
    a = [True] * limit
    a[0] = a[1] = False

    for (i, iscomposite) in enumerate(a):
        if not iscomposite:
            yield i
            # Mark factors non-prime
            for n in range(i, limit, i):
                a[n] = False

def main():
    for prime in prime_sieve(100):
        print(prime)
    for composite in composite_sieve(100):
        print(composite)

if __name__ == '__main__':
    main()
