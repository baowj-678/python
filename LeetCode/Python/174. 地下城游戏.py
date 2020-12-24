# 一些恶魔抓住了公主（P）并将她关在了地下城的右下角。
# 地下城是由 M x N 个房间组成的二维网格。我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。

# 骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。

# 有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；
# 其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。

# 为了尽快到达公主，骑士决定每次只向右或向下移动一步。

#  

# 编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。

# 例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。

# -2 (K)	-3	3
# -5	-10	1
# 10	30	-5 (P)
#  

# 说明:

# 骑士的健康点数没有上限。

# 任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/dungeon-game
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def calculateMinimumHP_(self, dungeon) -> int:
        height = len(dungeon)
        width = len(dungeon[0])
        for j in range(1, width):
            dungeon[0][j] += dungeon[0][j - 1]
        for i in range(1, height):
            dungeon[i][0] += dungeon[i - 1][0]
            for j in range(1, width):
                dungeon[i][j] += max(dungeon[i - 1][j], dungeon[i][j - 1])
        print(dungeon)
        for j in range(1, width):
            dungeon[0][j] = min(dungeon[0][j - 1], dungeon[0][j])
        for i in range(1, height):
            dungeon[i][0] = min(dungeon[i - 1][0], dungeon[i][0])
            for j in range(1, width):
                dungeon[i][j] = min(dungeon[i][j], max(dungeon[i - 1][j],
                                                       dungeon[i][j - 1]))
        print(dungeon)
        return (1 - dungeon[height - 1][width - 1])

    def calculateMinimumHP(self, dungeon) -> int:
        height = len(dungeon)
        width = len(dungeon[0])
        height -= 1
        width -= 1
        dungeon[height][width] = max(1, 1 - dungeon[height][width])
        for j in range(width - 1, -1, -1):
            dungeon[height][j] = max(1, dungeon[height][j + 1] - dungeon[height][j])
        height -= 1
        for i in range(height, -1, -1):
            dungeon[i][width] = max(1, dungeon[i + 1][width] - dungeon[i][width])
            for j in range(width - 1, -1, -1):
                dungeon[i][j] = max(1, min(dungeon[i + 1][j], dungeon[i][j + 1]) - dungeon[i][j])
        print(dungeon)
        return dungeon[0][0]


if __name__ == '__main__':
    dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    solution = Solution()
    print(solution.calculateMinimumHP(dungeon))
