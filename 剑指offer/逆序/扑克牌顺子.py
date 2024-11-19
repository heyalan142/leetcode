class Solution:
    def IsContinuous(self, numbers: list[int]) -> bool:
        numbers.sort()
        length = len(numbers)
        zeroCount = 0
        gap = 0
        for i in range(length - 1):
            if numbers[i] == 0:
                zeroCount += 1
            else:
                if numbers[i + 1] - numbers[i] == 0:
                    return False
                else:
                    gap += (numbers[i + 1] - numbers[i] - 1)
        if gap > zeroCount:
            return False
        else:
            return True


if __name__ == '__main__':
    numbers = [1, 3, 0, 7, 0]
    result = Solution().IsContinuous(numbers)
    print(result)
