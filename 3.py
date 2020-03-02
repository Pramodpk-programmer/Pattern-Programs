print("Third Number Pattern")
lastNumber = 6
for row in range(1, lastNumber):
    for column in range(row, 0, -1):
        print(column, end=' ')
    print("")


# Sample Output

# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1 