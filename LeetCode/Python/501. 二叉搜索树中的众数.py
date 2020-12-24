from LeetCode.tree import TreeNode

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.max_ = []
        self.maxTimes = 0
        self.lastTime = 0
        self.lastNum = None
        if root is None:
            return []
        self.findNum(root)

        if self.lastTime > self.maxTimes:
            self.maxTimes = self.lastTime
            self.max_.clear()
            self.max_.append(self.lastNum)
        elif self.lastTime == self.maxTimes:
            self.max_.append(self.lastNum)
        return self.max_

    def findNum(self, root):
        if root is None:
            return None
        if root.left is not None:
            self.findNum(root.left)
        if root.val == self.lastNum:
            self.lastTime += 1
        else:
            if self.lastTime > self.maxTimes:
                self.maxTimes = self.lastTime
                self.max_.clear()
                self.max_.append(self.lastNum)
            elif self.lastTime == self.maxTimes:
                self.max_.append(self.lastNum)
            self.lastNum = root.val
            self.lastTime = 1
        if root.right is not None:
            self.findNum(root.right)