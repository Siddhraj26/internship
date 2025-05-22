d={1:"python",2:"java",3:"react"}
d[2]="test"
print(d)


#clear()	Removes all the elements from the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)

#copy()	Returns a copy of the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.copy()
print(x)

#fromkeys()	Returns a dictionary with the specified keys and value
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)


#get()	Returns the value of the specified key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)


#items()	Returns a list containing a tuple for each key value pair
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)


#keys()	Returns a list containing the dictionary's keys
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)


#pop()	Removes the element with the specified key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)

#popitem()	Removes the last inserted key-value pair
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car)


#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)


#update()	Updates the dictionary with the specified key-value pairs
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print(car)


#values()	Returns a list of all the values in the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)