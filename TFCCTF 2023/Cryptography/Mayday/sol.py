#!/usr/bin/env python3

input = "Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash Yankee Oscar Uniform Dash Sierra One November Kilo India November Golf Dash Four Bravo Zero Uniform Seven".split()
flag = ""

nato_alphabet = {
    'Alpha': 'A', 'Bravo' : 'B', 'Charlie' : 'C', 'Delta' : 'D',
    'Echo' : 'E', 'Foxtrot' : 'F', 'Golf' : 'G', 'Hotel' : 'H',
    'India' : 'I', 'Juliett' : 'J', 'Kilo' : 'K', 'Lima' : 'L',
    'Mike' : 'M', 'November' : 'N', 'Oscar' : 'O', 'Papa' : 'P',
    'Quebec' : 'Q', 'Romeo' : 'R', 'Sierra' : 'S', 'Tango' : 'T',
    'Uniform' : 'U', 'Victor' : 'V', 'Whiskey' : 'W', 'X-Ray' : 'X',
    'Yankee' : 'Y', 'Zulu' : 'Z', 'Zero' : '0', 'One' : '1', 'Two' : '2',
    'Three' : '3', 'Four' : '4', 'Five' : '5', 'Six' : '6', 'Seven' : '7',
    'Eight' : '8', 'Nine' : '9', 'Dash' : '-'
}

for i in input:
    if not i in list(nato_alphabet.keys()):
        print(f'Cannot translate this char {i}')
    else:
        flag += nato_alphabet[i]

print(f'TFCCTF{{{flag}}}')