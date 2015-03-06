'''Check if two strings are permutations of one another'''

def permutation_checker(a, b):
    '''Takes 2 strings and checks if they are permutations of one another'''
    if len(a) == len(b):
        # return sorted(a) == sorted(b)
        return all(a.count(char) == b.count(char) for char in a)
    else:
        return False
        
def main():
    input1, input2 = raw_input("Input two strings (or integers), separated by a space: ").split()
    print permutation_checker(input1, input2)
    
if __name__ == '__main__': 
     main()
