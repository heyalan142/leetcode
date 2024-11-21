# 用字典做
def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    table = {}
    res = set()
    for num in nums1:
        table[num] = table.get(num, 0) + 1
    for num in nums2:
        if num in table:
            res.add(num)
            del table[num]
    return list(res)


# 用集合set做
# def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
#     return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(intersection(nums1, nums2))
