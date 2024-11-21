'''
https://www.nowcoder.com/practice/cf7e25aa97c04cc1a68c8f040e71fb84?
tpId=13&tqId=23455&ru=/exam/oj/ta&qru=/ta/coding-interviews/question
-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13

思路：
迭代法。每个子树序列化为{-中-{-中-左-右-}-{-中-左-右-}-}的形式
反序列化的时候解析成{中，左子树，右子树}
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root) -> str:
        if not root:
            return None
        left = self.Serialize(root.left)
        right = self.Serialize(root.right)
        if left and right:
            return "{" + "-" + str(root.val) + "-" + left + "-" + right + "-" + "}"
        elif left and not right:
            return "{" + "-" + str(root.val) + "-" + left + "-" + "#" + "-" + "}"
        elif right and not left:
            return "{" + "-" + str(root.val) + "-" + "#" + "-" + right + "-" + "}"
        else:
            return "{" + "-" + str(root.val) + "-" + "#" "-" + "#" + "-" + "}"

    def Deserialize(self, s) -> TreeNode:
        if not s:
            return None
        stack = []
        spilts = s.split("-")
        for item in spilts:
            if item == "}":
                results = self.stackPopList(stack)
                if len(results) >= 3:
                    result = results[0]
                    if result.isdigit():
                        val = int(result)
                        node = TreeNode(val)
                        leftVal = results[1]
                        rightVal = results[2]
                        if type(leftVal) is TreeNode:
                            node.left = leftVal
                        elif leftVal != "#":
                            node.left = TreeNode(leftVal)
                        if type(rightVal) is TreeNode:
                            node.right = rightVal
                        elif rightVal != "#":
                            node.right = TreeNode(rightVal)
                        stack.append(node)
            else:
                stack.append(item)
        return stack[-1]

    def stackPopList(self, stack) -> list:
        results = []
        while stack:
            letter = stack.pop()
            if letter != "{":
                results.append(letter)
            else:
                break
        results.reverse()
        return results


if __name__ == '__main__':
    root = TreeNode(100)
    root.left = TreeNode(50)
    root.left.right = TreeNode(150)
    string = Solution().Serialize(root)
    root = Solution().Deserialize(string)
    print("f")
