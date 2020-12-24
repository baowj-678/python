import queue
# 107. 二叉树的层次遍历 II
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其自底向上的层次遍历为：

# [
#   [15,7],
#   [9,20],
#   [3]
# ]


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def setLeft(self, x):
        self.left = x

    def setRight(self, x):
        self.right = x

    def setVal(self, x):
        self.val = x


class Tree:
    def __init__(self):
        self.root = TreeNode(None)

    def buildTree(self, numList):
        if(len(numList) == 0):
            return None
        self.root.setVal(numList[0])
        rootList = queue.Queue()
        rootList.put(self.root)
        index = 1
        while(index < len(numList)):
            rootTemp = rootList.get()
            rootTemp.setLeft(TreeNode(numList[index]))
            rootList.put(rootTemp.left)
            index = index + 1
            if(index < len(numList)):
                rootTemp.setRight(TreeNode(numList[index]))
                rootList.put(rootTemp.right)
                index = index + 1
            else:
                break
        return self.root


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        Q = queue.Queue()
        Q.put(root)
        numList = []
        if(root is not None):
            Q.put(None)
            numList = [[]]
        while(Q.empty() is False):
            root = Q.get()
            if(root is None):
                if(Q.empty() is False):
                    numList.insert(0, [])
                    Q.put(None)
            else:
                numList[0].append(root.val)
                if(root.left is not None):
                    Q.put(root.left)
                if(root.right is not None):
                    Q.put(root.right)
        return numList


def main():
    numList = []
    # numList = np.random.randn(100)
    # numList = numList.tolist()
    tree = Tree()
    tree = tree.buildTree(numList)
    # print(tree.val)
    solution = Solution()
    print(solution.levelOrderBottom(tree))


main()
