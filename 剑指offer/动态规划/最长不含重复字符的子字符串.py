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
