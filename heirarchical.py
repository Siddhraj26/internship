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

class cricket(Player):
    def __init__(self, name, country,cric):
         self.name = name
         self.country = country
         self.cric = cric

    def display_cric(self):
        print({self.name}, "plays as a", {self.cric})

kohli = cricket("Virat Kohli", "India","Batsmen")
dhoni = cricket("Mahendrasingh Dhoni","India","Batsmen")
rohit = cricket("Rohit Sharma","India","Batsmen")

kohli.display_info()
kohli.display_cric()
print()

dhoni.display_info()
dhoni.display_cric()
print()

rohit.display_info()
rohit.display_cric()
print()
