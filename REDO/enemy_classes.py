class wchicken:
    def __init__(self): #Chicken classes for Chicken Mobs ~Implemented by Jihad
        self.mobname = "Warrior Chicken"
        self.hp = 55
        self.mp = 0
        self.dex = random.randint(3,4)

class mchicken:
    def __init__(self):
        self.mobname = "Mage Chicken"
        self.hp = 40
        self.mp = 30
        self.dex = 3
class rchicken:
    def __init__(self):
        self.mobname = "Rogue Chicken"
        self.hp = 40
        self.mp = 40
        self.dex = random.randint(5,6)
