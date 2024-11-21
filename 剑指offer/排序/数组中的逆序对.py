'''
https://www.nowcoder.com/practice/96bd6684e04a44eb80e6a68efc0ec6c5?
tpId=13&tqId=23260&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''


class Solution:
    def InversePairs(self, nums: list[int]) -> int:
        if len(nums) <= 0:
            return 0
        lastNum = nums.pop()
        results = self.dfs(nums, lastNum)
        count = 0
        for pair in results:
            if len(pair) == 2:
                count += 1
        return count

    def dfs(self, nums: list[int], input: int) -> list[list[int]]:
        results = [[input]]
        if len(nums) <= 0:
            return results
        lastNum = nums.pop()
        pairs = self.dfs(nums, lastNum)
        for pair in pairs:
            if len(pair) == 2:
                if input < pair[-1]:
                    results.append([pair[-1], input])
                    results.append([pair[0], input])
                elif pair[-1] < input < pair[0]:
                    results.append([pair[0], input])
                results.append(pair)
            elif len(pair) == 1:
                if input < pair[-1]:
                    results.append([pair[-1], input])
                else:
                    results.append(pair)
        return results


if __name__ == '__main__':
    data = [1, 2, 3]
    result = Solution().InversePairs(data)
    print(result)
