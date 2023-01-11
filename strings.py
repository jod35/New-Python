str1 = "Jonathan"
print(str1)

print("she said, \"You are a good person.\"")

str2 = """This
text
fills 
many lines
++++====>>>>
"""

print(str2)

print(f"{str2} has a length of {len(str2)}")

print(str1.lower())
print(str2.capitalize())
print(str2.removeprefix("This"))
print(str2.removesuffix(">>>>"))


#encode 
print(type(str1.encode("utf-8")))

#create a bytes object
print(b"Yo boy")


sentence = "The problem is yout think you have a lot of time."

print(sentence[0]) #T
print(sentence[8]) #l

print(sentence[14:40]) #yout think you have a lot