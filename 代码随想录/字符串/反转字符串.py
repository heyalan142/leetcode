def reverseString(s: list[str]) -> list[str]:
    left = 0
    right = len(s) - 1
    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1
    return s


if __name__ == "__main__":
    print(reverseString(["h", "e", "l", "l", "o"]))
