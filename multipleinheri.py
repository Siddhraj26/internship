class Ronaldo:
    def skills(self):
        print ("Ronaldo: Excellent dribbling and powerful shots.")

class Messi:
    def skills(self):
        print("Messi: Incredible vision and precise passing.")

class Neymar(Ronaldo, Messi):
    def skills(self):
        print("a")
    
player = Neymar()
player.skills()