""" Morris遍历二叉树 算法
@Author: Bao Wenjie
@Email: bwj_678@qq.com
@Date: 2020/9/29
"""


class TreeNode():
    """ 二叉树数据结构
    """
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def preorderTraversal(root: TreeNode):
    ans = []
    cur = root
    if root.left is None:
        ans.append(root.val)
        cur = cur.right
    else:
        pre = cur.left
        while pre.right is not None and pre.right is not cur:
            pre = pre.right
        if pre.right is None:
            ans.append(pre.val)
            pre.right = cur
        else:
            pre.right = None
            cur = cur.right


def inorderTraversal(root: TreeNode):
    cur = root
    ans = []
    if cur.left is None:
        ans.append(cur.val)
        cur = cur.right
    else:
        pre = cur.left
        while pre.right is not None and pre.right is not cur:
            pre = pre.right
        if pre.right is None:
            pre.right = cur
        else:
            pre.right = None
            ans.append(cur.val)
            cur = cur.right


def postorderTraversal(root: TreeNode):
    cur = root
    ans = []
    if cur.left is None:
        cur = cur.right
    else:
        pre = cur.left
        while pre.right is not None and pre.right is not cur:
            pre = pre.right
        if pre.right is None:
            pre.right = root
        else:
            pre.right = None
            tmp = []
            tmp_p = cur.left
            while tmp_p is not cur:
                tmp.append(tmp_p.val)
                tmp_p = tmp_p.right
            ans += tmp[::-1]
            cur = cur.right
