class Ships:
    def __init__(self):
        self.items = []

    def choose_ship(self):
        print("1. Titanic Ship - Rs.20,000/-\n2. US Navy War Ship - Rs.50,000/-")
        ships = int(input("Which type of ship you want: "))

        if ships == 1:
            price = 20000
            tax = 2000
            final_price = price + tax
            self.items.append(("Titanic Ship", final_price))
            print("Added Titanic Ship - Rs.", final_price)

        elif ships == 2:
            price = 50000
            tax = 3000
            final_price = price + tax
            self.items.append(("US Navy War Ship", final_price))
            print("Added US Navy War Ship - Rs.", final_price)

        else:
            print("Select a valid product!")

        return self.items
