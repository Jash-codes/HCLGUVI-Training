class Cars:
    def __init__(self):
        self.items = []

    def choose_car(self):
        print("1. Aston Martin - Rs.60,000/-\n2. Ferrari - Rs.40,000/-")
        cars = int(input("Which type of car you want: "))

        if cars == 1:
            price = 60000
            tax = 4000
            final_price = price + tax
            self.items.append(("Aston Martin", final_price))
            print("Added Aston Martin - Rs.", final_price)

        elif cars == 2:
            price = 40000
            tax = 2000
            final_price = price + tax
            self.items.append(("Ferrari", final_price))
            print("Added Ferrari - Rs.", final_price)

        else:
            print("Select a valid product!")

        return self.items
