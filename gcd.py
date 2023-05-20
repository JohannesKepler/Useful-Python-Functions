'''Input (int1, int2); Output gcd as int.'''

def gcd(a, b):
    if a > b:
        a, b = b, a
    while True:
        mod = b % a
        if mod == 0:
            return a
        b, a = a, mod
        
def main():
    input1, input2 = input("Input two numbers, separated by a space: ").split()
    print(gcd(int(input1), int(input2)))
    
if __name__ == '__main__':
    main()
