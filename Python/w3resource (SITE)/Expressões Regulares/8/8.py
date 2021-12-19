import re

def cheque(string):
    if re.findall('[A-Z][a-z]', string):
        return 'Match!'
    return 'Not a match!'

print(cheque('AaBbGg'))  # Match!
print(cheque('Python'))  # Match!
print(cheque('python'))  # Not a Match!
print(cheque('PYTHON'))  # Not a Match!
print(cheque('aA'))  # Not a Match!
print(cheque('Aa'))  # Match!
