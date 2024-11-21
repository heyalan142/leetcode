def isAnagram(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    record = [0] * 26
    for string in str1:
        record[ord(string) - ord("a")] += 1

    for string in str2:
        record[ord(string) - ord("a")] -= 1

    for num in record:
        if num != 0:
            return False
    return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))
