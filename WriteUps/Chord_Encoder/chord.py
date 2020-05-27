import re

dict = {
    '0112': 'A',
    '2110': 'B',
    '1012': 'C',
    '020': 'D',
    '0200': 'E',
    '1121': 'F',
    '001': "G",
    '0122': 'a',
    '2100': 'b',
    '1002': 'c',
    '010': 'd',
    '0100': 'e',
    '1011': 'f',
    '000': 'g'
}

a = ""
with open('decoded_sheet.txt', 'r') as file:
    for word in file:
        sword = re.sub('[^0-9]', '', word)
        a = a+dict[sword]

print a
