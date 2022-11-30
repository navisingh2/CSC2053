# Navi Singh
# my_functions.py

# Should take a list parameter and return the mean in integer form.
def means(my_list):
    sum_of = 0
    for i in my_list:
        sum_of += i
    return sum_of // len(my_list)

# Returns the even numbers from a list
def get_even(list):
    return [x for x in list if x % 2 == 0]

# Calling Function #1:
my_list = [10, 20, 30, 40, 50]
print("The mean of ", my_list, " is: ", means(my_list))
my_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print("The mean of ", my_list, " is: ", means(my_list))
my_list = [23, 45, 67, 84, 97, 12]
print("The mean of ", my_list, " is: ", means(my_list))

print() #space in between

# Calling Function #2:
new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The even numbers of ", new_list, " is ", get_even(new_list))
new_list = [10, 15, 20, 25, 30, 35, 40, 45, 50]
print("The even numbers of ", new_list, " is ", get_even(new_list))
new_list = [24, 33, 57, 68, 93, 102, 110]
print("The even numbers of ", new_list, " is ", get_even(new_list))
