#creating sets

#a set of numbers
s1 = {1,2,3}

#an empty set
s2=set()

print(s1)
print(s2)

#adding items to a set
s2.add(1)
s2.add(2)

print(s2)

a= {1,2,3,4,5,6,8}
b = {2,3,5,9,10,12,123}

print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

