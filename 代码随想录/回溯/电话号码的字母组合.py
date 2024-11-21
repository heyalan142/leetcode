class Solution:
    def __init__(self):
        self.letterMap = [
            "",  # 0
            "",  # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs",  # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
        self.result = []
        self.string = ""

    def backtracking(self, digits: str, index: int) -> None:
        if index == len(digits):
            self.result.append(self.string)
            return
        digit = int(digits[index])
        letters = self.letterMap[digit]
        for i in range(len(letters)):
            self.string += letters[i]
            self.backtracking(digits, index + 1)
            self.string = self.string[:-1]

    def letter_combinations(self, digits: str):
        if len(digits) == 0:
            return self.result
        self.backtracking(digits, 0)
        return self.result


if __name__ == '__main__':
    solution = Solution()
    print(solution.letter_combinations("23"))
