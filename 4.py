print("Fourth Number Pattern")
lastNumber = 12
for i in range(1, lastNumber):
    for j in range(-1+i, -1, -1):
        # print(format(j**2, "4d"), end='')
        print(format(2**j, "4d"), end=' ')
    print("")


# Sample Output

#    1 
#    2    1 
#    4    2    1 
#    8    4    2    1 
#   16    8    4    2    1 
#   32   16    8    4    2    1 
#   64   32   16    8    4    2    1 
#  128   64   32   16    8    4    2    1 
#  256  128   64   32   16    8    4    2    1 
#  512  256  128   64   32   16    8    4    2    1 
# 1024  512  256  128   64   32   16    8    4    2    1 