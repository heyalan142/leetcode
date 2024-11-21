def is_valid(string: str) -> bool:
    stack = []
    for item in string:
        if item == "{":
            stack.append("}")
        elif item == "[":
            stack.append("]")
        elif item == "(":
            stack.append(")")
        elif len(stack) == 0 or stack[-1] != item:
            return False
        else:
            stack.pop()

    if len(stack) > 0:
        return False
    else:
        return True


if __name__ == '__main__':
    ex1 = "()"
    ex2 = "()[]{}"
    ex3 = "(]"
    ex4 = "([)]"
    ex5 = "{[]}"
    print(is_valid(ex1))
    print(is_valid(ex2))
    print(is_valid(ex3))
    print(is_valid(ex4))
    print(is_valid(ex5))
