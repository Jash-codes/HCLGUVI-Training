print("Select the type of operation")

print("1. ADDITION (+)")
print("2. SUBTRACTION (-)")
print("3. MULTIPLICATION (*)")
print("4. DIVISION (/)")

choice = input("Enter Choicec(+, -, *, /): ")

num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second number: "))

if choice == "+":
    result = num1+num2
    print(f"{num1} + {num2} = {result}")

elif choice == "-":
    result = num1-num2
    print(f"{num1} - {num2} = {result}")

elif choice == "*":
    result = num1*num2
    print(f"{num1} * {num2} = {result}")

elif choice == "/":
    result = num1/num2
    print(f"{num1} / {num2} = {result}")

else:
    print("invalid operation selected ")