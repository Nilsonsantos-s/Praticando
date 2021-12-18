import re


def cheque(string):
    if re.match('ab{3}', string):
        return 'Match!'
    return 'Not a match!'

print(cheque('x'))