class Player:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def display_info(self):
        print("Player:" ,{self.name}, "Country:" ,{self.country})

class footballer(Player):
    def __init__(self, name, country, position,awards):
        super().__init__(name, country)
        self.position = position
        self.awards= awards

    def display_position(self):
        print({self.name}, "plays as a", {self.position},{self.awards})

class awards(footballer):
    def __init__(self, name, country, position,awards):
        super().__init__(name, country, position)
        self.awards=awards
    
    def display_awards(self):
        print({self.name},"Awards",{self.awards})


class starfootballer(footballer):
    def __init__(self, name, country, position,awards):
        super().__init__(name, country, position,awards)

    def display_starfootballer(self):
        print({self.name},"Player details",{self.awards})
            
        
       
ronaldo = starfootballer("Cristiano Ronaldo", "Portugal", "Right wing","Golden boot & Best player")
messi = starfootballer("Lionel Messi", "Argentina", "Left wing","Golden boot & Best player")
neymar = starfootballer("Neymar Jr", "Brazil", "Right wing","Golden boot & Best player")


ronaldo.display_info()
ronaldo.display_position()
ronaldo.display_starfootballer()
print()

messi.display_info()
messi.display_position()
messi.display_starfootballer
print()

neymar.display_info()
neymar.display_position()
neymar.display_starfootballer()
print()

 




 