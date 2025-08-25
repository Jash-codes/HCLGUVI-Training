def lego():
    print("Select Lego Category")

    cat = int(input("1.Ships \n2.Cars\n Enter your choice: "))
    
    if (cat == 1):
        print("1.Titanic Ship - Rs.20,000/-\n2.US navy war ship - Rs.50,000/-")
        ships = int(input("Which type of ship u want : "))
        if ships == 1:
            price = 20000
            tax = 2000
            final_price = price + tax
            print("the final price of the product is Rs.",final_price," /- including taxes")
    
        elif ships == 2:
            price = 50000
            tax = 3000
            final_price = price + tax
            print("the final price of the product is Rs.",final_price,"/ -including taxes")

        else:
            print("select a valid Product")

    if (cat == 2):
        print("1.Aston Martin - Rs.60,000/-\n2.Ferrari - Rs.40,000/-")
        cars = int(input("Which type of car u want : "))
        if cars == 1:
            price = 60000
            tax = 4000
            final_price = price + tax
            print("the final price of the product is Rs.",final_price," /- including taxes")
        
        elif (cat == 2):
            price = 40000
            tax = 2000
            final_price = price + tax
            print("the final price of the product is Rs.",final_price,"/ -including taxes")

        else:
            print("select a valid Product")        
lego()
       
