import re


def cheque(string):
    if re.match('^[a-z]+_[a-z]+$', string):
        return 'Match!'
    return 'Not a match!'

print(cheque('aab_abbbc'))

