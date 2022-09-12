# Printing prime numbers in a range
lower = 2
upper = 48
for num in range(lower, upper+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num) #prime