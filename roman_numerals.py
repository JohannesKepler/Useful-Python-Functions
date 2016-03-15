'''A function to convert from Roman to Arabic Numerals,
    and another to convert back'''

ROME = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
ARABIA = [1, 5, 10, 50, 100, 500, 1000]
RANK = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

def get_arabic(roman_num):
    '''Takes a Roman Numeral (string)
    and converts to Arabic Numeral (integer)'''
    roman_num = list(roman_num)
    num_score = 0
    for i in range(len(roman_num)):
        letter = roman_num[i]
        try:
            next_letter = roman_num[i+1]
            if RANK.index(letter) < RANK.index(next_letter):
                num_score -= ROME[letter]
            else:
                num_score += ROME[letter]
        except:
            num_score += ROME[letter]
    return num_score

def get_roman(arabic_num):
    '''Takes an integer and converts to a Roman Numeral (string)'''
    roman_num = []
    for arabic in ARABIA[::-1]:
        roman_num.append(arabic_num / arabic)
        arabic_num -= arabic * roman_num[len(roman_num)-1]
    roman_num.reverse()
    for idx in range(len(roman_num)-1):
        if roman_num[idx] > 3:
            roman_num[idx] = 1
            roman_num[idx+1] += 1
    roman_str = ''
    for roman_idx in range(len(roman_num)):
        roman_str += RANK[roman_idx] * roman_num[roman_idx]
    roman_str = roman_str[::-1]
    if 'VVI' in roman_str:
        roman_str = roman_str.replace('VVI', 'IX')
    if 'LLX' in roman_str:
        roman_str = roman_str.replace('LLX', 'XC')
    if 'DDC' in roman_str:
        roman_str = roman_str.replace('DDC', 'CM')

    return roman_str

def main():
    which_way = raw_input("1. Roman -> Arabic\n2. Arabic -> Roman\n")
    if which_way == "1":
        r_to_a = raw_input("Please enter Roman numeral: ")
        try:
            print get_arabic(r_to_a)
        except:
            print "Try again, friend."
    elif which_way == "2":
        a_to_r = raw_input("Please enter Arabic numeral (integer): ")
        try:
            a_to_r = int(a_to_r)
            print get_roman(a_to_r)
        except:
            print "Try a positive integer, friend."
    else:
        print "Try again, friend."
    
if __name__ == "__main__":
    main()
