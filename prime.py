num = int(input("enter a number:"))

for i in range(2,num):
    if (num % i) == 0:
        print(f"{num}, its not a prime number")
    else:
        print("its a prime number")
        break