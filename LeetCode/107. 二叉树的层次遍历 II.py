import queue


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
        self.root.setVal = numList[0]
        rootList = queue.Queue()
        rootList.put(self.root)
        for 
        self.buildTreeInner(numList, 1, rootList)
        return self.root

    def buildTreeInner(self, numList, index, rootList):
        if(index == len(numList) - 1):

        pass



class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        pass
