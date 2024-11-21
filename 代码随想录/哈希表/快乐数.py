def sumForSplitNum(num: int) -> int:
    splits = []
    while num > 0:
        splits.append(num % 10)
        num = num // 10
    result = 0
    for item in splits:
        result += item * item
    return result


def isHappy(num: int) -> bool:
    # 题目中说了会 无限循环，那么也就是说求和的过程中，sum会重复出现，这对解题很重要！
    # 这道题目使用哈希法，来判断这个sum是否重复出现，如果重复了就是return false， 否则一直找到sum为1为止。
    record = set()
    while True:
        num = sumForSplitNum(num)
        if num == 1:
            return True
        else:
            if num in record:
                return False
            else:
                record.add(num)



if __name__ == "__main__":
    num = 18
    print(isHappy(num))
