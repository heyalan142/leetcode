class Solution:
    def findDuplicateNums(self, numbers: list[int]) -> int:
        hash_map = dict()
        for num in numbers:
            if num not in hash_map.keys():
                hash_map[num] = 1
            else:
                return num
        return -1


if __name__ == '__main__':
    input = [2, 3, 1, 0, 2, 5]
    print(Solution().findDuplicateNums(input))
