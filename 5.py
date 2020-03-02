print("Fifth Number Pattern")
lastNumber = 9
for i in range(1, lastNumber):
    for i in range(0, i, 1):
        print(format(2**i, "4d"), end=' ')
    for i in range(-1+i, -1, -1):
        print(format(2**i, "4d"), end=' ')
    print("")


# Sample Output

#    1 
#    1    2    1 
#    1    2    4    2    1 
#    1    2    4    8    4    2    1 
#    1    2    4    8   16    8    4    2    1 
#    1    2    4    8   16   32   16    8    4    2    1 
#    1    2    4    8   16   32   64   32   16    8    4    2    1 
#    1    2    4    8   16   32   64  128   64   32   16    8    4    2    1 