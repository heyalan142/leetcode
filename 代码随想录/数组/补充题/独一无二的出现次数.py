def unique_occurrences(nums: [int]) -> bool:
    table = dict()
    for i, num in enumerate(nums):
        table[num] = table.get(num, 0) + 1
    value_list = sorted(table.values())
    for i in range(len(value_list) - 1):
        if value_list[i] == value_list[i + 1]:
            return False
    return True


if __name__ == '__main__':
    nums = [1, 2, 2, 1, 1, 3]
    result = unique_occurrences(nums)
    print(result)
