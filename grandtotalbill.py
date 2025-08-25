import datetime

def lego():
    items = []   
    grand_total = 0

    while True:
        print("\nSelect Lego Category")
        cat = int(input("1. Ships \n2. Cars \n3. Exit & Generate Bill\nEnter your choice: "))

        if cat == 1:
            print("1. Titanic Ship - Rs.20,000/-\n2. US Navy War Ship - Rs.50,000/-")
            ships = int(input("Which type of ship you want: "))
            if ships == 1:
                price = 20000
                tax = 2000
                final_price = price + tax
                items.append(("Titanic Ship", final_price))
                print("Added Titanic Ship - Rs.", final_price)
            
            elif ships == 2:
                price = 50000
                tax = 3000
                final_price = price + tax
                items.append(("US Navy War Ship", final_price))
                print("Added US Navy War Ship - Rs.", final_price)
            
            else:
                print("Select a valid product!")

        elif cat == 2:
            print("1. Aston Martin - Rs.60,000/-\n2. Ferrari - Rs.40,000/-")
            cars = int(input("Which type of car you want: "))
            if cars == 1:
                price = 60000
                tax = 4000
                final_price = price + tax
                items.append(("Aston Martin", final_price))
                print("Added Aston Martin - Rs.", final_price)
            
            elif cars == 2:
                price = 40000
                tax = 2000
                final_price = price + tax
                items.append(("Ferrari", final_price))
                print("Added Ferrari - Rs.", final_price)
            
            else:
                print("Select a valid product!")

        elif cat == 3:
            break 
        
        else:
            print("Invalid category! Try again.")

    if items:
        now = datetime.datetime.now()
        filename = "lego_bill.txt"

        with open(filename, "a") as f:  
            f.write("\n=========== LEGO STORE BILL ===========\n")
            f.write("Date & Time: " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
            f.write("--------------------------------------\n")
            
            for product, cost in items:
                f.write(f"{product:20} Rs.{cost}\n")
                grand_total += cost

            f.write("--------------------------------------\n")
            f.write(f"Grand Total:         Rs.{grand_total}\n")
            f.write("======================================\n")
        
        print("\nBill generated successfully! Check 'lego_bill.txt'.")
    else:
        print("No items purchased. Bill not generated.")

lego()
