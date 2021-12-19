import re


def cheque(string):
    if re.findall('^[a]\S+b+$', string):
        return 'Match!'
    return 'Not a match!'

print(cheque("aabbbbd"))  # Not a match!
print(cheque("aabAbbbc"))  # Not a match!
print(cheque("accddbbjjjb"))  # Match!
