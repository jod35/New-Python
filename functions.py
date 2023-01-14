#functions arer the building blocks of code
#they help us execute commonly done tasks\

#simple function
def hello():
    print("Hello")

hello()


#function with return value
def sum_of_list(num_list):
    total = 0

    for num in num_list:
        total+=num

    return total


sum_=sum_of_list([1,2,3,4])
print(sum_)

def max_of_numbers(x,y,z):
    if (x > y) and (x > z):
        return x

    elif (y > x) and (y> z):
        return y

    else:
        return z

print(max_of_numbers(12,123,4))
        