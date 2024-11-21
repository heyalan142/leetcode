def find_content_children(g: [int], s: [int]) -> int:
    g.sort  # 将孩子的贪心因子排序
    s.sort  # 将饼干的尺寸排序
    index = len(s) - 1
    result = 0
    for i in range(len(g) - 1, -1, -1):
        if index >= 0 and s[index] >= g[i]:  # 遍历饼干
            result += 1
            index -= 1
    return result


if __name__ == '__main__':
    g = [1, 2]
    s = [1, 2, 3]
    result = find_content_children(g, s)
    print(result)
