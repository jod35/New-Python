#functions arer the building blocks of code
#they help us execute commonly done tasks\

#simple function
def hello():
    print("Hello")

hello()


#function with return value
def sum_of_list(num_list):
    """
    The sum_of_list function adds up all the numbers in a list and returns the sum.
    
    Parameters:
    num_list (list): A list of integers to be added together. 
    
    
    :param num_list: Pass a list of numbers to the function
    :return: The sum of all the numbers in a list
    :doc-author: jod35
    """
    total = 0

    for num in num_list:
        total+=num

    return total


sum_=sum_of_list([1,2,3,4])
print(sum_)

def max_of_numbers(x,y,z):
    """
    The max_of_numbers function returns the maximum of three numbers.
    
    Parameters:
    x (int): The first number to compare.
    y (int): The second number to compare.
    z (int): The third number to compare.  
    
    :param x: Store the first number, y is used to store the second number and z is used to store the third number
    :param y: Determine the maximum value of x and z
    :param z: Determine which of the two numbers is greater
    :return: The largest of the three numbers
    :doc-author: jod35
    """
    if (x > y) and (x > z):
        return x

    elif (y > x) and (y> z):
        return y

    else:
        return z

print(max_of_numbers(12,123,4))

def multiply_all_numbers_in_list(list_of_numbers):
    """
    The multiply_all_numbers_in_list function multiplies all the numbers in a list of numbers.
    
    Parameters:
        list_of_numbers (list): A list of integers or floats.  The elements are multiplied together and the result is returned.
    
    
    :param list_of_numbers: Pass a list of numbers to the function
    :return: The product of all numbers in a list
    :doc-author: jod35
    """
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
    """
    The calculate_lowercase_and_uppercase function accepts a string and returns the number of lowercase and uppercase characters in the string.
       The function will return two values: (uppercase,lowercase)
    
    :param word: Store the string that is passed in to the function
    :return: The number of lowercase and uppercase letters in a given string
    :doc-author: jod35
    """
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
    """
    The get_even_numbers function returns a list of even numbers from the input list.
       
    
    :param list_num: Pass a list of numbers to the function
    :return: A list of even numbers from the input list
    :doc-author: jod35
    """
    
    result = []
    for i in list_num:
        if i % 2 == 0:
            result.append(i)

    return result

print(get_even_numbers([1,2,3,4,5,6,7,8]))