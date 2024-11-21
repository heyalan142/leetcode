'''
https://www.nowcoder.com/practice/c451a3fd84b64cb19485dad758a55ebe?
tpId=13&tqId=23251&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
思路：
从某一个数字开始的连续序列和等于目标数如果有，只能有一个，于是我们可以用这个性质来使区间滑动。
两个指针l、r指向区间首和区间尾，计算区间内部的序列和，如果这个和刚好等于目标数，说明以该区间首开始的序列找到了，
记录下区间内的序列，同时以左边开始的起点就没有序列了，于是左区间收缩；如果区间和大于目标数，说明该区间过长需要收缩，
只能收缩左边；如果该区间和小于目标数，说明该区间过短需要扩大，只能向右扩大，移动区间尾。

具体做法：
step 1：从区间[1,2]开始找连续子序列。
step 2：每次用公式计算区间内的和，若是等于目标数，则记录下该区间的所有数字，为一种序列，同时左区间指针向右。
step 3：若是区间内的序列和小于目标数，只能右区间扩展，若是区间内的序列和大于目标数，只能左区间收缩。
'''


class Solution:
    def FindContinuousSequence(self, sum: int) -> list[list[int]]:
        left = 1
        right = 2
        results = []
        while left < right:
            curSum = self.getSum(left, right)
            if curSum == sum:
                result = []
                for i in range(left, right + 1):
                    result.append(i)
                results.append(result)
                left += 1
            elif curSum > sum:
                left += 1
            elif curSum < sum:
                right += 1
        return results

    def getSum(self, left: int, right: int) -> int:
        current = left
        sum = 0
        while current <= right:
            sum += current
            current += 1
        return sum


if __name__ == '__main__':
    sum = 0
    val = Solution().FindContinuousSequence(sum)
    print(val)
