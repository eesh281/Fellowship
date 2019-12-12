def paren_balanced(paren_string):
    stack = []
    for i in paren_string:
        if i == "[" or i == "{" or i == "(":
            stack.append(i)
        elif i == "]" or i == "}" or i == ")":
            stack.pop()
    if len(stack) == 0:
        print(True)
    else:
        print(False)


paren_string = input("enter expression: ")
paren_balanced(paren_string)
