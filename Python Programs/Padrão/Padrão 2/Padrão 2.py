copiax = str(1)
for c in range(0, 5):
    if c > 0:
        copiay = c+1
        copiay = str(copiay)
        copiax= copiax + copiay
        print(' '.join(copiax))
    else:
        print(copiax)
        
        
        
