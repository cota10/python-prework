# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
# The first line of code has been defined as below

def hello_name(user_name):
    print("Hello_" + user_name.title() + "!")

user_name = input("Enter Username: ")

hello_name(user_name)


# Question 2 
# Write a python function, first_odds that prints the odd numbers 1-100 and returns nothing

def first_odds():
    for i in range(1,101):
        if i % 2 != 0:
            print(i)

first_odds()


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.
#  The first line of the code has been defined as below.

def max_num_in_list(list):
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return max

list = [1, 2, 3, 4, 5, 6]

print(max_num_in_list(list))


# Question 4 
# Write a function to return if the given year is a leap year.
#  A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(year):
    if year % 4 == 0:
        return True
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return False
year = int(input())
print(is_leap_year(year))


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
# the return should be boolean type.

def is_consecutive(list_0):
    return sorted(list_0) == list(range(min(list_0), max(list_0)+1))

list_0 = [2,3,4,5,6,7]
print(is_consecutive(list_0))
list_0 = [1,2,4,5]
print(is_consecutive(list_0))