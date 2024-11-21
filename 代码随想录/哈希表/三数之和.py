# 递归法
def computeSums(input_nums, target_value, current_count, result, temp_result=[]):
    num_len = len(input_nums)
    for index in range(num_len):
        current_value = input_nums[index]
        temp_result.append(current_value)
        if current_count == 1:
            if current_value == target_value:
                result.append(temp_result[:])
        else:
            temp_input = input_nums[index + 1:]
            computeSums(temp_input, target_value - current_value, current_count - 1, result, temp_result)
        temp_result.pop()

# 双指针法
# def threeNum(nums: list[int]) -> list[list]:
#     result = []
#     nums.sort()
#     for i in range(len(nums)):
#         if nums[i] > 0:
#             return result
#         if i + 1 < len(nums) and nums[i + 1] == nums[i]:
#             continue
#
#         left = i + 1
#         right = len(nums) - 1
#
#         while left < right:
#             if nums[i] + nums[left] + nums[right] > 0:
#                 right -= 1
#             elif nums[i] + nums[left] + nums[right] < 0:
#                 left += 1
#             else:
#                 result.append([nums[i], nums[left], nums[right]])
#                 # 跳过相同的元素以避免重复
#                 while right > left and nums[right] == nums[right - 1]:
#                     right -= 1
#                 while right > left and nums[left] == nums[left + 1]:
#                     left += 1
#                 left += 1
#                 right -= 1
#
#     return result


if __name__ == "__main__":
    input = [-1, 0, 1, 1, 1, 1, 1, 1, 1]
    result = []
    computeSums(input, 0, 3, result)
    # result = threeNum(input)
    print(result)
