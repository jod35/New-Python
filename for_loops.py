numbers =[0,1,2,3,4,5]

for number in numbers:
    print(number)


for number in range(5):
    print(number)


print([x for x in range(5)])

print([x for x in range(0,5)])

print([x for x in range(0,20,2)])

names =['Jonathan',"Jerry","Jordan","Aba","Preach"]


for i in range(len(names)):
    print(i,names[i])

print("\n")

for position, item in enumerate(names):
    print(position,item)


people = ['Nick','Rick','Roger','Syd']
ages = [23,24,25,21]


for position in range(len(people)):
    person = people[position]
    age = ages[position]

    print(f"{person} {age}")
