import re


def cheque(string):
    if re.match('ab{2,3}', string):
        return 'Match!'
    return 'Not a match!'

print(cheque('abb'))