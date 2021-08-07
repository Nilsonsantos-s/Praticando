for c in range(1, 6):
    if c > 1:
        if c == 2:
            print(c, c-1)
        elif c == 3:
            print(c, c-1, c-1*2)
        elif c == 4:
            print(c, c-1, c-1*2, c-1*3)
        else:
            print(c, c-1, c-1*2, c-1*3, c-1*4)
    else:
        print(c)




