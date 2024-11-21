def fourSumCount(nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
    hashmap = dict()
    for num1 in nums1:
        for num2 in nums2:
            total = num1 + num2
            if total in hashmap:
                hashmap[total] += 1
            else:
                hashmap[total] = 1
    count = 0
    for num3 in nums3:
        for num4 in nums4:
            total = num3 + num4
            key = 0 - total
            if key in hashmap:
                count += hashmap[key]
    return count


if __name__ == '__main__':
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(fourSumCount(A, B, C, D))
