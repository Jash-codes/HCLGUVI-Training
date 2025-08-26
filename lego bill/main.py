import datetime
from ships import Ships
from cars import Cars


def lego():
    items = []
    grand_total = 0

    while True:
        print("\nSelect Lego Category")
        cat = int(input("1. Ships \n2. Cars \n3. Exit & Generate Bill\nEnter your choice: "))

        if cat == 1:
            s = Ships()
            items.extend(s.choose_ship())

        elif cat == 2:
            c = Cars()
            items.extend(c.choose_car())

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
            
            f.close()
        
        print("\nBill generated successfully! Check 'lego_bill.txt'.")
    else:
        print("No items purchased. Bill not generated.")


if __name__ == "__main__":
    lego()
