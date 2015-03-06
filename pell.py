'''Pell's equation: x^2-D*y^2=1'''

from continuous_fraction import cont_frac
from math import sqrt

# reduce a list representation of a repeating fraction to a
# whole number fraction, where the numerator and denominator
# are the x and y of the above Pell equation, respectively
def pell(d, cont_frac_repr):
    '''Input a continued fraction represented as a list, eg:
    sqrt(7): [2, 1, 1, 1, 4]
    Output list approximation: [numerator, denominator]'''
    if sqrt(d) == int(sqrt(d)):
        raise ValueError("No possible solution for perfect square D")

    def sub_pell(cont_frac_repr):
        '''Helper function implements algorithm to reduce continued fraction
        representation to a single numerator/denominator list'''
        if len(cont_frac_repr) % 2 == 0:
            cont_frac_repr.append(1)
        else:
            cont_frac_repr[-1] = 1

        while True:
            temp_val = cont_frac_repr[-3] * cont_frac_repr[-2]
            temp_val = temp_val + cont_frac_repr[-1]
            cont_frac_repr[-3] = temp_val
            cont_frac_repr = cont_frac_repr[:-1]

            if len(cont_frac_repr) == 2:
                return cont_frac_repr

    # make a copy to avoid unintentionally altering list
    cont_frac_copy = list(cont_frac_repr)

    check_solution = sub_pell(cont_frac_repr)
    # check if it solves the Pell equation
    if check_solution[0]**2 - d * check_solution[1]**2 == 1:
        return check_solution
    # if not, you need one more repetition of the continued fraction
    else:
        cont_frac_copy.extend(cont_frac_copy[1:])
        check_solution = sub_pell(cont_frac_copy)
        return check_solution

if __name__ == '__main__':
    print "Pell equation: x^2 - D*y^2 = 1\n"
    user_input_2 = int(raw_input("Input D to find fundamental solution for: "))
    cont_frac_input = cont_frac(user_input_2)
    pell_solution = pell(user_input_2, cont_frac_input)
    print "D = %d" % user_input_2
    print "x = %d" % pell_solution[0]
    print "y = %d" % pell_solution[1]
