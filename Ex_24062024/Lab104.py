# Filter in Python
# The filter() function in Python is a built-in function
# allows you to filter elements in the list, tuple, set.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Filter on the above -> even ->
# new_list_Even = [2, 4, 6, 8, 10]


def is_even(num):
    return num % 2 == 0


def greater_5(num):
    return num > 5


# new_numbers_even = filter(is_even, numbers)
new_numbers_five = filter(greater_5, numbers)
print(list(new_numbers_five))

####################

number1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(num):
    return num % 2 == 0


num_number1 = filter(is_even, number1)
print("These are even numbers", (list(num_number1)))

#########################

##Define a function to filter strings longer than 3 characters

words = ['Shobha', 'Naidu', 'Van', 'Sre', 'Lakshmi', 'Ishu', 'cat', 'mat']

def len_string(string):
    return len(string) > 3

lenOfString = filter(len_string, words)
print(list(lenOfString))


lenOfString = list(filter(lambda string : len(string) > 3, words))
print(list(lenOfString))

##########################

#Filtering None Values from a List

data = [1, None, 3, None, 5, None, 7]

# def is_none(data):
#     return data == "None"

dataWithNoNone = filter(None, data)
print(list(dataWithNoNone))

#################################

#Define a function to filter names starting with 'A'

names = ["Alice", "Bob", "Anna", "Alex", "David", "Amy"]

def nameStartsA(name):
    return name.startswith("A")

nameStartsWithA = filter(nameStartsA, names)
print(list(nameStartsWithA))