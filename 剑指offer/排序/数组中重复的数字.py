class Solution:
    def duplicate(self, numbers: list[int]) -> int:
        hashMap = dict()
        for num in numbers:
            if num in hashMap:
                return num
            else:
                hashMap[num] = 1
        return -1


if __name__ == '__main__':
    data = [2, 3, 1, 0, 2, 5, 3]
    result = Solution().duplicate(data)
    print(result)
