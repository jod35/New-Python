a=[1,2,3,4]

#adding to the  end of a list
a.append(5) #[1, 2, 3, 4, 5]

print(a)

#adding to a certain index
a.insert(1,2) #[1, 2, 2, 3, 4, 5]

print(a)

#counts unique occurences of a member in a list
print(a.count(2))

#extend the list by another
a.extend([5,6,7,8])
print(a)

#find the index of an item in a list

print(a.index(3)) #3

#remove first occurence of item from a list
a.remove(2)

a.remove(5)

print(a)

#reverse a list
a.reverse()

print(a)