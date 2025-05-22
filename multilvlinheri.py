class Player:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def display_info(self):
        print("Player:" ,{self.name}, "Country:" ,{self.country})

class Footballer(Player):
    def __init__(self, name, country, position):
        super().__init__(name, country)
        self.position = position

    def display_position(self):
        print({self.name}, "plays as a", {self.position})

class StarFootballer(Footballer):
    def __init__(self, name, country, position):
        super().__init__(name, country, position)
       
ronaldo = StarFootballer("Cristiano Ronaldo", "Portugal", "Right wing")
messi = StarFootballer("Lionel Messi", "Argentina", "Left wing")
neymar = StarFootballer("Neymar Jr", "Brazil", "Right wing")

ronaldo.display_info()
ronaldo.display_position()
print()

messi.display_info()
messi.display_position()
print()

neymar.display_info()
neymar.display_position()
print()
