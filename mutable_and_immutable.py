age = 45

print(age) # returns 45
print(id(age)) #first id

#reassign the value 

age = 53

print(age) #prints 53
print(id(age))#second id

#here we can notice that the values of variables can change including the ids


class Man:
    def __init__(self,name) -> None:
        self.name = name

man1 = Man(name="JONA")

print(id(man1))

print(id(man1))

print(id(man1.name))


man1.name ="Jonathan"
print(id(man1.name)) #change in the value and change in id