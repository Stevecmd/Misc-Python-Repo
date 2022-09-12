num = int(input("Please enter a number : "))
if num < 1:
    print("not a prime number.")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} - is not a prime number")
            break
    else:
        print(f"{num} - Is a prime number")