class Solution:
    def FirstNotRepeatingChar(self, str: str) -> int:
        hashTable = dict()
        for s in str:
            if s in hashTable:
                hashTable[s] += 1
            else:
                hashTable[s] = 1
        for i in range(len(str)):
            if hashTable[str[i]] == 1:
                return i
        return -1


if __name__ == '__main__':
    string = "google"
    val = Solution().FirstNotRepeatingChar(string)
    print(val)
