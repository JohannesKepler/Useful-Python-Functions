'''Continued Fractions: Return list representation of sqrt(n)'''
from math import sqrt

def cont_frac(n):
    '''Find coefficients of repeating fraction of sqrt(n)'''
    # equations of the form:
    # a + sqrt(n) - b
    #     -----------
    #          c
    if int(sqrt(n)) == sqrt(n):
        return [1]
    a = []
    b = []
    c = []

    # a[0]:
    a.append(int(sqrt(n)))
    # insert blanks for b[0] and c[0] to get indices to align:
    b.append(0)
    c.append(0)

    # a[1], b[1], c[1]:
    c.append(n - a[0]**2)
    a.append(int(1/(sqrt(n) - a[-1])))
    b.append(abs(a[0] - a[1]*c[1]))
    # print a, b, c
    # compute the rest, stop when the new alignment has already been found:
    while True:
        # a[-1] means a(i-1), a_next means a(i)
        c_next = (n - b[-1]**2)/c[-1]
        a_next = int((sqrt(n) + b[-1]) / c_next)
        b_next = abs(b[-1] - c_next * a_next)
        # print a_next, b_next, c_next
        if a_next == a[1] and b_next == b[1] and c_next == c[1]:
            break
        a.append(a_next)
        b.append(b_next)
        c.append(c_next)
    return a

def main():
    print("Returns continuous fraction for sqrt(n)")
    user_input_2 = int(input("Input n: "))
    print(cont_frac(user_input_2))


if __name__ == '__main__':
    main()
