#Set
c={1,2,3}
c[1]=0
print(c)


#add() Adds an element to the set
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

#clear()	 	Removes all the elements from the set
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

#copy()	 	Returns a copy of the set
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)


#difference()	-	Returns a set containing the difference between two or more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)


#difference_update()	-=	Removes the items in this set that are also included in another, specified set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)


#discard()	 	Remove the specified item
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)


#intersection()	&	Returns a set, that is the intersection of two other sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)


#intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)


#isdisjoint()	 	Returns whether two sets have a intersection or not
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)


#issubset()	<=	Returns whether another set contains this set or not
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)


#issuperset()	>=	Returns whether this set contains another set or not
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)


#pop()	 	Removes an element from the set
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)


#remove()	 	Removes the specified element
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)


#symmetric_difference()	^	Returns a set with the symmetric differences of two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)


#symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)


#union()	|	Return a set containing the union of sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)


#update()	|=	Update the set with the union of this set and others
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)
