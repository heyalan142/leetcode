def get_next_value(s: str) -> int:
    left = 0
    right = len(s) - 1
    value = 0
    while left < right:
        if s[left] == s[right]:
            value += 1
        else:
            break
        left += 1
        right -= 1
    return value


def get_next_list(s: str) -> list[int]:
    next = []
    for i in range(1, len(s) + 1):
        sub_str = s[0:i]
        next_value = get_next_value(sub_str)
        next.append(next_value)
    return next

def get_next_list(s: str) -> list[int]:
    next = []
    for i in range(1, len(s) + 1):
        sub_str = s[0:i]
        next_value = get_next_value(sub_str)
        next.append(next_value)
    return next

def str_str(str1:str, str2:str) -> str:
    i = 0
    j = 0
    next_list = get_next_list(str1)
    while i < len(str1) and j < len(str2):
        while i > 0 and str1[i] != str2[j]:
            i = next_list[i-1]
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            j += 1
        if i == len(str1):
            return str2[j-len(str1):]








if __name__ == "__main__":
    needle = "aabaaf"
    haystack = "aabaabaafa"
    print(str_str(needle, haystack))

