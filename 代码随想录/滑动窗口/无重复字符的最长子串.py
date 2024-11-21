def longest_substring_length(char: str) -> int:
    left = 0
    hash_set = set()
    longest_length = 0
    for right in range(len(char)):
        right_char = char[right]
        if right_char not in hash_set:
            hash_set.add(right_char)
            longest_length = max(longest_length, right - left + 1)
        else:
            while right_char in hash_set:
                left_char = char[left]
                hash_set.remove(left_char)
                left += 1
            hash_set.add(right_char)
    return longest_length


if __name__ == '__main__':
    char = "pwwkew"
    result = longest_substring_length(char)
    print(result)
