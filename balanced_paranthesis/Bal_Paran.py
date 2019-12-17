# *********************************************************************************************************************************************
# @purpose :Implement Balanced Parenthesis Using LinkedList
# @file    :Bal_Paran.py
# @author  :GursheeshKour
# *********************************************************************************************************************************************

# this method determines whether parenthesis are balanced or not
def paren_balanced(expression_):
    stack = []
    for i in expression_:
        if i == "[" or i == "{" or i == "(":
            stack.append(i)
        elif i == "]" or i == "}" or i == ")":
            stack.pop()
    if len(stack) == 0:
        print(True)
    else:
        print(False)

#taking the arithematic expression as input
expression_ = input("enter expression: ")
#calling the method
paren_balanced(expression_)
