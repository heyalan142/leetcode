def sorted_squares(nums: list[int]) -> list:
    left = 0
    right = len(nums) - 1
    index = len(nums) - 1
    square_list = [float('inf')] * len(nums)
    while left <= right:
        left_result = nums[left] * nums[left]
        right_result = nums[right] * nums[right]
        if left_result < right_result:
            square_list[index] = right_result
            right -= 1
        else:
            square_list[index] = left_result
            left += 1
        index -= 1
    return square_list


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    result = sorted_squares(nums)
    print(result)
