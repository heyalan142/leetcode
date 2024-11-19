class Solution:
    def GetLeastNumbers_Solution(self, input: list[int], k: int) -> list[int]:
        if k == 0 or len(input) == 0:
            return []
        else:
            input.sort()
            return input[:k]


if __name__ == '__main__':
    input = [4, 5, 1, 6, 2, 7, 3, 8]
    k = 4
    result = Solution().GetLeastNumbers_Solution(input, 4)
    print(result)
