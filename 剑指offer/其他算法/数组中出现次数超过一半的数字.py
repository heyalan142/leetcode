
class Solution:
    def MoreThanHalfNum_Solution(self, numbers: list[int]) -> int:
        length = len(numbers)
        hashMap = dict()
        for num in numbers:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
            if hashMap[num] > length / 2:
                return num
        return -1


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    val = Solution().MoreThanHalfNum_Solution(nums)
    print(val)
