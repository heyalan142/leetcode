'''
https://www.nowcoder.com/practice/6aa9e04fc3794f68acf8778237ba065b?tpId=13&
tqId=23296&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-ranking&sourceUrl
=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13
'''


class Solution:
    # 丑数：只含有因子：2,3,5
    # 1是第1个丑数
    # 分析：1 2x1 3x1 2x2 5x1 2x3 2x2x2 3x3x3 2x5
    def GetUglyNumber_Solution(self, index):  # 求第index个丑数
        if index <= 1:
            return index
        uglys = [1]
        # 前面生成的每一个丑数都应该乘以2，3，5以产生新的丑数，但是我们不必比较前面的每一个丑数
        # 例如：假设前面的某个丑数a 因为乘以2 得到了当前的丑数b，下一次再生成下一个丑数时，就不用再考察a以及a前面的丑数*2的情况了，
        # 但是还要a乘以3或5的情况，以及前面的除了a以外的其他丑数（可能在a前面或后面）乘以2，3，5的情况
        idx2, idx3, idx5 = 0, 0, 0  # idx2表示上一个 是因为乘以2而产生的丑数的下标，其他依次类推
        for i in range(1, index):
            cur_ugly = min(uglys[idx2] * 2, uglys[idx3] * 3, uglys[idx5] * 5)
            uglys.append(cur_ugly)
            if cur_ugly % 2 == 0:
                idx2 += 1
            if cur_ugly % 3 == 0:
                idx3 += 1
            if cur_ugly % 5 == 0:
                idx5 += 1
        return uglys[-1]


if __name__ == '__main__':
    val = Solution().GetUglyNumber_Solution(7)
    print(val)
