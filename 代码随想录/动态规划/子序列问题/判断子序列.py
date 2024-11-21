#双指针法
# def check_sub_seq(source, target):
#     len_s = len(source)
#     len_t = len(target)
#     i = 0
#     j = 0
#     result = 0
#     while i < len_s and j < len_t:
#         if source[i] == source[j]:
#             result = result + 1
#             j = j + 1
#         i = i + 1
#
#     return result == len_t

#动态规划法
def check_sub_seq(source, target):
    dp = [[0] * (len(target)+1) for _ in range(len(source)+1)]
    for i in range(1, len(source)+1):
        for j in range(1, len(target)+1):
            if source[i-1] == target[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = dp[i][j - 1]

    if dp[-1][-1] == len(source):
        return True
    return False


if __name__ == '__main__':
    s = "axc"
    t = "ahbgdc"
    print(check_sub_seq(s, t))



