def canConstruct(ransomNote: str, magazine: str) -> bool:
    record = {}
    for letter in magazine:
        num = ord(letter) - ord('a')
        record[num] = record.get(num, 0) + 1
    for letter in ransomNote:
        num = ord(letter) - ord('a')
        record[num] = record.get(num, 0) - 1
    for key, value in record.items():
        if value < 0:
            return False
    return True

if __name__ == "__main__":
    print(canConstruct("aa", "aab"))
