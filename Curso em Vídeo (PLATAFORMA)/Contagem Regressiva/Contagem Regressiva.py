import time
print('===CONTAGEM REGRESSIVA===')
print('Lançamento de fogos de artíficio')
for c in range (10, -1, -1):
    if c == 0:
        print('BOOM!')
    else:
        print(c)
    time.sleep(1)

