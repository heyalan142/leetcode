'''
https://www.nowcoder.com/practice/48d2ff79b8564c40a50fa79f9d5fa9c7?
tpId=13&tqId=2276769&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13

具体做法:
step 1：构建一个哈希表，用于统计字符元素出现的次数。
step 2：窗口左右界都从字符串首部开始，每次窗口优先右移右界，并统计进入窗口的元素的出现频率。
step 3：一旦右界元素出现频率大于1，就需要右移左界直到窗口内不再重复，将左边的元素移除窗口的时候同时需要将它在哈希表中的频率减1，保证哈希表中的频率都是窗口内的频率。
step 4：每轮循环，维护窗口长度最大值。
'''


class Solution:
    # 滑动窗口：先右边遍历移动，发现右边字符串重复把左边向前移动到不重复位置
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxLength = 0
        hashMap = dict()
        while right < len(s):
            if s[right] in hashMap:
                hashMap[s[right]] += 1
            else:
                hashMap[s[right]] = 1
            while hashMap[s[right]] > 1:
                hashMap[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
            right += 1
        return maxLength


if __name__ == '__main__':
    string = "abcabcbb"
    val = Solution().lengthOfLongestSubstring(string)
    print(val)
