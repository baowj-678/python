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

    def setRoot(self, root):
        self.root = root

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

    def getRoot(self):
        return self.root

    def levelOrderBottom(self):
        Q = queue.Queue()
        Q.put(self.root)
        numList = []
        if(self.root is not None):
            Q.put(None)
            numList = [[]]
        while(Q.empty() is False):
            self.root = Q.get()
            if(self.root is None):
                if(Q.empty() is False):
                    numList.insert(0, [])
                    Q.put(None)
            else:
                numList[0].append(self.root.val)
                if(self.root.left is not None):
                    Q.put(self.root.left)
                if(self.root.right is not None):
                    Q.put(self.root.right)
        return numList
