'''
https://www.nowcoder.com/practice/762836f4d43d43ca9deb273b3de8e1f4?
tpId=13&tqId=23252&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13

思路：
我们需要的顺子是连续的，那我们就对数组先进行一次排序，可以当作任意牌的0，都在前面，后面的如果是顺子就应该是连续的。
遍历数组，遇到零牌计数，遇到非零牌计算与其后的间隔数，最后比较零牌数与间隔数，若是间隔数大于零牌数则不能组成顺子。

step 1：优先对数组排序。
step 2：遍历数组，遇到零牌计数，遇到非零牌统计其与后一个是否相同，因为重复非零牌不能构成顺子。
step 3：计算当前非零牌与后一张相邻牌的间隔，并将所有间隔累加。
step 4：间隔数大于零牌数，则无法构成顺子。
'''


class Solution:
    def IsContinuous(self, numbers: list[int]) -> bool:
        numbers.sort()
        length = len(numbers)
        zeroCount = 0
        gap = 0
        for i in range(length - 1):
            if numbers[i] == 0:
                zeroCount += 1
            else:
                if numbers[i + 1] - numbers[i] == 0:
                    return False
                else:
                    gap += (numbers[i + 1] - numbers[i] - 1)
        if gap > zeroCount:
            return False
        else:
            return True


if __name__ == '__main__':
    numbers = [1, 3, 0, 7, 0]
    result = Solution().IsContinuous(numbers)
    print(result)
