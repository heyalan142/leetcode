def remove_duplicates(string: str) -> str:
    stack = []
    for item in string:
        if len(stack) > 0 and item == stack[-1]:
            stack.pop()
        else:
            stack.append(item)
    return "".join(stack)


if __name__ == '__main__':
    ex1 = "abbaca"
    print(remove_duplicates(ex1))
