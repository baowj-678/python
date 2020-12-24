# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

#  

# 参考以下这颗二叉搜索树：

#      5
#     / \
#    2   6
#   / \
#  1   3
# 示例 1：

# 输入: [1,6,3,2,5]
# 输出: false
# 示例 2：

# 输入: [1,3,2,6,5]
# 输出: true

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def verifyPostorder(self, postorder: list) -> bool:
        if len(postorder) <= 1:
            return True
        max_ = postorder[-1]
        split = -1
        i = 0
        for i in range(len(postorder) - 1):
            if postorder[i] >= max_:
                if split == -1:
                    split = i
            else:
                if split != -1:
                    return False
        if split == -1:
            split = 0
        return self.verifyPostorder(postorder[0:split]) and self.verifyPostorder(postorder[split:len(postorder) - 1])


if __name__ == "__main__":
    solution = Solution()
    postorder = [1, 2, 5, 10, 6, 9, 4, 3]
    print(solution.verifyPostorder(postorder))
