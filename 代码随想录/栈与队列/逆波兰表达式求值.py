import math


def eval_rpn(splits: list) -> list:
    stack = []
    for string in splits:
        if string == "+":
            stack.append(stack.pop() + stack.pop())
        elif string == "-":
            stack.append(stack.pop() - stack.pop())
        elif string == "*":
            stack.append(stack.pop() * stack.pop())
        elif string == "/":
            num1 = stack.pop()
            num2 = stack.pop()
            num3 = math.ceil(num2/num1)
            stack.append(num3)
        else:
            stack.append(int(string))

    return stack.pop()




if __name__ == '__main__':
    # splits1 = ["2", "1", "+", "3", "*"]
    # print(eval_rpn(splits1))
    # splits2 = ["4", "13", "5", "/", "+"]
    # print(eval_rpn(splits2))
    splits3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(eval_rpn(splits3))
