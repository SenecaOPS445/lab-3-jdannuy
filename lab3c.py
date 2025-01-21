#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: Jhanlyn Brita Dannuy

def operate(number1, number2, operator):
    if operator == 'add':
        return int(number1) + int(number2)
    elif operator == 'subtract':
        return int(number1) - int(number2)
    elif operator == 'multiply':
        return int(number1) * int(number2)
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    print(operate(10, 5, 'add'))  # Output: 15
    print(operate(10, 5, 'subtract'))  # Output: 5
    print(operate(10, 5, 'multiply'))  # Output: 50
    print(operate(10, 5, 'divide'))  # Output: Error message
