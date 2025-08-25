# MULTILEVEL INHERITANCE

class gp():
    def __init__(self):
        self.gold = "---"
        self.land = "---"
    

    def landgp(self):
        land = "10cr"
        self.land = land

    def goldgp(self):
        gold = "2kg"
        self.gold = gold

class parent(gp):

    def __init__(self):
        self.bike = "---"
        self.house = "---"

    def bikep(self):
        bike = "GT"
        self.bike = bike
        bike2 = "triumph"
        self.bike2 = bike2

    def housep(self):
        house = "1800sqf"
        self.house = house

class child(parent):
    def __init__(self):
        self.bikep()
        self.housep()
        self.landgp()
        self.goldgp()
    def c1(self):
        print(self.bike)
        print(self.bike2)

    def c2(self):
        print(self.house)
        print(self.land)
        print(self.gold)
        
obj = child()

obj.c1()

obj2 = child()

obj2.c2()