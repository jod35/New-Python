simple_dict={} #empty dictionary

print(simple_dict)

#creating a dictionary object
my_dict =dict()
print(my_dict) #print an empty dictionary

#a dictionary with items
person1 ={
    'name':"Ruth",
    'age':23,
    'nationality':'Ugandan'
}

print(person1)

#we can also add items to a dict by providing keys with values
simple_dict['person_1']="Ruth"
simple_dict['person_2']="Jerusha"

print(simple_dict)


#accessing items in a dictionary can be done by using keys
print(person1['age'])

print(person1['name'])


#we can also check for whether some items are kept in dictionary by using keys
print('name' in person1) #True if it exists

print('course' in person1) #False if does not exist


# we can also clear a dictionary by using the clear method
simple_dict.clear()

print(simple_dict) #{}