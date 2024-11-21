'''
https://www.nowcoder.com/practice/11662ff51a714bbd8de809a89c481e21?
tpId=13&tqId=2282583&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-
ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
递归+滑动窗口
思路：
dp数组表示以下标i为终点的最大连续子数组和，则每次遇到一个新的数组元素，连续的子数组要么加上变得更大，要么它本身就更大，因此状态转移为
dp[i]=max(dp[i−1]+array[i],array[i])，这是最基本的求连续子数组的最大和。但是题目要求需要返回长度最长的一个，我们则每次用left、
right记录该子数组的起始，需要更新最大值的时候（要么子数组和更大，要么子数组和相等的情况下区间要更长）顺便更新最终的区间首尾，这样我们的
区间长度就是最长的。

具体做法：
step 1：创建动态规划辅助数组，记录到下标i为止的最大连续子数组和，下标为0的时候，肯定等于原数组下标为0的元素。
step 2：准备左右区间双指针记录每次连续子数组的首尾，再准备两个双指针记录最大和且区间最长的连续子数组的首尾。
step 3：遍历数组，对于每个元素用上述状态转移公式记录其dp值，更新区间首尾（如果需要）。
step 4：出现一个最大值。且区间长度更大的时候，更新记录最长区间的双指针。
step 5：根据记录的最长子数组的位置取数组。

'''

class Solution:

    # 递归法：dp[i]为求得最大和子数组最后一位一定是array[i]的数组的最大值
    def FindGreatestSumOfSubArray(self, array: list[int]) -> list[int]:
        # write code here
        dp = [0 for _ in range(len(array))]
        dp[0] = array[0]
        left = 0
        right = 0
        maxSum = dp[0]
        maxLeft = 0
        maxRight = 0
        for i in range(1, len(array)):
            right += 1
            # 关键代码，dp[i - 1] + array[i] 要大于等于，包括等于 array[i]。因为等于的时候dp[i - 1] + array[i]长度最长
            if dp[i - 1] + array[i] >= array[i]:
                dp[i] = dp[i - 1] + array[i]
            else:
                dp[i] = array[i]
                left = right
            if maxSum < dp[i] or (maxSum == dp[i] and right -left > maxRight - maxLeft):
                maxSum = dp[i]
                maxLeft = left
                maxRight = right
        return array[maxLeft:maxRight + 1]


if __name__ == '__main__':
    nums = [1, 2, -3, 4, -1, 1, -3, 2]
    val = Solution().FindGreatestSumOfSubArray(nums)
    print(val)
