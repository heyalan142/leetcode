def commonChars(words: list[str]) -> list[str]:
    if not words:
        return []
    hash_first = [0] * 26
    for s in words[0]:
        hash_first[ord(s) - ord("a")] += 1

    for index in range(1, len(words)):
        hash_other = [0] * 26
        for sting in words[index]:
            hash_other[ord(sting) - ord("a")] += 1
        for k in range(26):
            hash_first[k] = min(hash_first[k], hash_other[k])
    result = []
    for i in range(26):
        while hash_first[i] != 0:  # 注意这里是while，多个重复的字符
            result.extend(chr(i + ord('a')))
            hash_first[i] -= 1
    return result


if __name__ == "__main__":
    words = ["bella", "label", "roller"]
    result = commonChars(words)
    print(result)
