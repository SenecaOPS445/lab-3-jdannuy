#!/usr/bin/env python3

# Declare a global list
my_list = [100, 200, 300, 'six hundred']

def give_list():
    # Return all items in my_list unchanged
    return my_list

def give_first_item():
    my_list = [100, 200, 300]  # Example list
    return str(my_list[0])

def give_first_and_last_item():
    # Return a list with the first and last items of my_list
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    # Return a list with the second and third items of my_list
    return my_list[1:3]

if __name__ == '__main__':
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())

