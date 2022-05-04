def multi_bracket_validation(input_str):
    # declare an empty list
    stack = []

    # Iterate over the input string
    for character in input_str:
        # If the input string contains an opening bracket then push it to the list
        if character == "(" or character == "[" or character == "{":
            stack.append(character)
        else:
            # in the case of valid brackets the stack can't be empty,
            # so if a closing bracket is encountered run this if
            if not stack:
                return False
            else:
                # if the input string contains a closing bracket
                # then pop the correct opening bracket from the stack (if it exists)
                top = stack[-1]
                if character == ')' and top == '(' or character == ']' and top == '[' or character == '}' and top == '{':
                    stack.pop()
    # Check the status of the stack to determine the validity of the string
    if not stack:
        return True
    else:
        return False



