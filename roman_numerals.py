'''Given list of a roman numerals, find most efficient method
    of writing number and calculate number of numerals
    saved by doing so'''

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
    # read in text file
    romans = [line.strip() for line in open("p089_roman.txt", 'r')]

    # convert from roman to arabic and back again,
    # to get most efficient roman numeral
    new_rome = []
    for numeral in romans:
        arab = get_arabic(numeral)
        roman = get_roman(arab)
        new_rome.append(roman)

    # count differences in string length
    difference = 0
    for idx_rome in range(len(new_rome)):
        difference += len(romans[idx_rome]) - len(new_rome[idx_rome])

    print difference
    
if __name__ == "__main__":
    main()
