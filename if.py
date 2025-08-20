unit = int(input("Enter the unit : "))
bill = 0



if 0 <= unit <=100 :
    bill = 0
    print("Your bill is free ")
    
elif 100 < unit <=300 :
    chargeable_units = unit - 100
    bill = chargeable_units*3
    print(f"Total bill is {bill}")

elif 300 < unit <=500 :
    chargeable_units = unit - 100
    bill = chargeable_units*3
    print(f"Total bill is {bill}")
