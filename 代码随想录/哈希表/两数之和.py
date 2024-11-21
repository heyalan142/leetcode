def twoSum(nums: list[int], target: int) -> list[int]:
    records = dict()
    result = []
    for index, num in enumerate(nums):
        if num in records:
            indexs = list()
            indexs.append(records[num])
            indexs.append(index)
            result.append(indexs)
        else:
            value = target - num
            records[value] = index
    return result


if __name__ == '__main__':
    nums = [2, 7, 4, 5, 11, 15]
    target = 9
    result = twoSum(nums, target)
    print(result)
