import array as arr
a=arr.array("d",[1,2,3]) #way to import array in a list
print(a) 


footballers=["Ronaldo","Messi","Neymar"]      # way to print the array
print(footballers)

footballers=["Ronaldo","Messi","Neymar"]
k= footballers[0]
print(k)                                      #way to print the specfic element from the array


footballers=["Ronaldo","Messi","Neymar"]
footballers[1]="Bale"
print(footballers)                            #way to change the  specific element of the array 


footballers=["Ronaldo","Messi","Neymar"]
k=len(footballers)
print(k)                                      #way to find out the number of elements present in array


footballers=["Ronaldo","Messi","Neymar"]
for x in footballers:
    print(x)                                  #way to use the for in looping statement in array


footballers=["Ronaldo","Messi","Neymar"]
footballers.append("Bale")
print(footballers)                            #way to add new element to array


footballers=["Ronaldo","Messi","Neymar","Bale"]
footballers.pop(2)
print(footballers)                            #way to remove specific element by it's index


footballers=["Ronaldo","Messi","Neymar","Bale"]
footballers.remove("Bale")
print(footballers)                             #way to remove specific element by it's name



footballers=["Ronaldo","Messi","Neymar","Bale"]
footballers.clear()
print(footballers)                             #way to remove the whole list of elements


footballers=["Ronaldo","Messi","Neymar","Bale"]
k=footballers.copy()
print(k)                                        #way to copy whole list


footballers=["Ronaldo","Messi","Neymar","Bale","Ronaldo"]
k=footballers.count("Ronaldo")
print(k)                                       #way to show how a specific element in list is repeated again & again 


footballers=["Ronaldo","Messi","Neymar","Bale"]
cars = ['Bugatti', 'Ferrai', 'Lamborghini']
footballers.extend(cars)
print(footballers)                              #way to extend or merge 2 lists


footballers=["Ronaldo","Messi","Neymar","Bale"]
k=footballers.index("Messi")
print(k)                                        #way to show the index number of specific element


footballers=["Ronaldo","Messi","Neymar","Bale"]
footballers.insert(1,"Marcelo")
print(footballers)                              #way to insert element in a list


footballers=["Ronaldo","Messi","Neymar","Bale"]
footballers.reverse()
print(footballers)                             #way to reverse the whole list of elements

footballers=["Ronaldo","Messi","Neymar","Bale"]
footballers.sort()
print(footballers)                             #way to sort the whole list of elements into the right order
