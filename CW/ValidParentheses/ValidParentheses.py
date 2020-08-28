# Valid Parentheses

# Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid.
# The function should return true if the string is valid, and false if it's invalid.

def valid_parentheses(string):
    brackets = 0
    for str in string:
        if str == '(':
            brackets += 1
        if str == ')' and brackets > 0:
            brackets -= 1
        elif str == ')' and brackets == 0:
            return False
    if brackets == 0:
        return True
    else:
        return False
