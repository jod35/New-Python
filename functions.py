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

def multiply_all_numbers_in_list(list_of_numbers):
    result = 1

    for number in list_of_numbers:
        result*=number

    return result

print(multiply_all_numbers_in_list([1,2,3,4,5]))
        

def check_number_in_range(num,range_):
    if num in range(0,range_):
        return True

    else:
        return False

print(check_number_in_range(2,10))

def calculate_lowercase_and_uppercase(word):
    up_total = 0
    low_total = 0



    for i in word:
        if i.isalpha():
            if i.islower():
                low_total+1
            elif i.isupper():
                up_total+1
        else:
            print("No characters")

    return up_total,low_total

print(calculate_lowercase_and_uppercase("WANNA FIGHT mate?"))


def get_even_numbers(list_num):
    result = []
    for i in list_num:
        if i % 2 == 0:
            result.append(i)

    return result

print(get_even_numbers([1,2,3,4,5,6,7,8]))