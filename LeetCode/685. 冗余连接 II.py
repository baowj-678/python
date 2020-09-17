# 在本问题中，有根树指满足以下条件的有向图。该树只有一个根节点，所有其他节点都是该根节点的后继。每一个节点只有一个父节点，除了根节点没有父节点。

# 输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

# 结果图是一个以边组成的二维数组。 每一个边 的元素是一对 [u, v]，用以表示有向图中连接顶点 u 和顶点 v 的边，其中 u 是 v 的一个父节点。

# 返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。

# 示例 1:

# 输入: [[1,2], [1,3], [2,3]]
# 输出: [2,3]
# 解释: 给定的有向图如下:
#   1
#  / \
# v   v
# 2-->3
# 示例 2:

# 输入: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# 输出: [4,1]
# 解释: 给定的有向图如下:
# 5 <- 1 -> 2
#      ^    |
#      |    v
#      4 <- 3
# 注意:

# 二维数组大小的在3到1000范围内。
# 二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/redundant-connection-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def findRedundantDirectedConnection(self, edges: list) -> list:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        last_edge = None
        cicle_edge = None
        unionFind = UnionFind(n + 1)
        for edge in edges:
            # 判断是否矛盾
            if parent[edge[1]] == edge[1]:
                parent[edge[1]] = edge[0]
                # 判断是否有环
                if unionFind.find(edge[0]) != unionFind.find(edge[1]):
                    unionFind.union(edge[0], edge[1])
                else:
                    cicle_edge = edge
            else:
                last_edge = edge
        if last_edge is None:
            return cicle_edge
        elif cicle_edge is None:
            return last_edge
        else:
            return [parent[last_edge[1]], last_edge[1]]


class UnionFind:
    def __init__(self, n: int):
        super().__init__()
        self.ancestor = [i for i in range(n)]

    def union(self, a, b):
        tmp = self.find(b)
        while self.ancestor[a] != a:
            anc = self.ancestor[a]
            self.ancestor[a] = tmp
            a = self.ancestor[anc]
        self.ancestor[a] = tmp

    def find(self, a):
        while self.ancestor[a] != a:
            a = self.ancestor[a]
        return a


if __name__ == "__main__":
    solution = Solution()
    edges = [[1, 2], [1, 3], [2, 3]]
    print(solution.findRedundantDirectedConnection(edges))
