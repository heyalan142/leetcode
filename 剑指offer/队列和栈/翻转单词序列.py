class Solution:
    def ReverseSentence(self, str: str) -> str:
        words = str.split(" ")
        while "" in words:
            words.remove("")
        left = 0
        right = len(words) - 1
        while left < right:
            temp = words[left]
            words[left] = words[right]
            words[right] = temp
            left += 1
            right -= 1
        return " ".join(words)


if __name__ == '__main__':
    str = "nowcoder. a am I"
    reverseStr = Solution().ReverseSentence(str)
    print(reverseStr)
