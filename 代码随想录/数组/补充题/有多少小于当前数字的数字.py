def smaller_numbers_than_current(nums: [int]) -> list[int]:
    res = nums[:]
    nums.sort()
    hash_table = dict()
    for i, num in enumerate(nums):
        if num not in hash_table.keys():
            hash_table[num] = i
    for i, num in enumerate(res):
        res[i] = hash_table[num]
    return res


if __name__ == '__main__':
    nums = [6, 5, 4, 8]
    target = 2
    result = smaller_numbers_than_current(nums)
    print(result)
