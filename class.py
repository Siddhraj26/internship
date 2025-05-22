class footballers:
    k="Ronaldo"
p1=footballers()
print(p1.k)                                      #creating a class


class footballers:
    def __init__(player,name,position):
        player.name=name
        player.position=position
p1= footballers("Ronaldo","RW")
print(p1.name)
print(p1.position)                               #making use of __init__()


class footballers:
    def __init__(player, name, age):
        player.name = name
        player.age = age

    def ronaldo(player):
        print("Hello my name is " + player.name)

p1 = footballers("Cristiano Ronaldo", 39) 
p1.ronaldo()                                     #adding multiple functions in a class


class footballers:
    def __init__(player,name,age):
        player.name=name
        player.age=age

    def ronaldo(player):
        print("Hello my name is"+player.name)
    p1=footballers("Cristiano",39)
    p1.age=40
    print(p1.age)                                #this is how we modify the value of the object in the class



class footballers:
    def __init__(player,name,age):
        player.name=name
        player.age=age
    def ronaldo(player):
        print("Hello my name is"+player.name)
    p1=footballers("Cristiano Ronaldo",39)
    del footballers.age
print(footballers.age)	                         #this is how we can delete any object in class      



class footballers:
    pass






