def reserveWord(word: str) -> str:
    words = word.split(" ")
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


if __name__ == "__main__":
    s = "the sky is blue"
    t = "  hello world!  "
    w = "a good   example"
    print(reserveWord(s))
    print(reserveWord(t))
    print(reserveWord(w))
