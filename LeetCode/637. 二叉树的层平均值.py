# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

#  

# 示例 1：

# 输入：
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 输出：[3, 14.5, 11]
# 解释：
# 第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
#  

# 提示：

# 节点值的范围在32位有符号整数范围内。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/average-of-levels-in-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from tree import TreeNode
import queue


class Solution:
    def averageOfLevels(self, root: TreeNode) -> list:
        Q = queue.Queue()
        Q.put(root)
        Q.put(None)
        average = []
        sum_ = 0
        count = 0
        while not Q.empty():
            tmp = Q.get()
            if tmp is None:
                average.append(sum_ / count)
                sum_ = 0
                count = 0
                if Q.empty():
                    break
                else:
                    Q.put(None)
            else:
                sum_ += root.val
                count += 1
                left = tmp.left
                right = tmp.right
                if left is not None:
                    Q.put(left)
                if right is not None:
                    Q.put(right)
        return average


if __name__ == "__main__":
    Q = queue.Queue()
    Q.put(9)
    Q.put(8)
    print(Q.get())
    print(Q.get())
    print(Q.empty())
