import re


def cheque(string):
    if re.match('ab?', string):
        return 'Match!'
    return 'Not a match!'

print(cheque('ax'))