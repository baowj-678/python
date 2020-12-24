# 给定一个表示分数的非负整数数组。 玩家 1 从数组任意一端拿取一个分数，随后玩家 2 继续从剩余数组任意一端拿取分数，然后玩家 1 拿，…… 。每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。

# 给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。

#  

# 示例 1：

# 输入：[1, 5, 2]
# 输出：False
# 解释：一开始，玩家1可以从1和2中进行选择。
# 如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）可选。
# 所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
# 因此，玩家 1 永远不会成为赢家，返回 False 。
# 示例 2：

# 输入：[1, 5, 233, 7]
# 输出：True
# 解释：玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。
#      最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 True，表示玩家 1 可以成为赢家。
#  

# 提示：

# 1 <= 给定的数组长度 <= 20.
# 数组里所有分数都为非负数且不会大于 10000000 。
# 如果最终两个玩家的分数相等，那么玩家 1 仍为赢家。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/predict-the-winner
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def PredictTheWinner(self, nums) -> bool:
        if len(nums) % 2 == 0:
            return True
        [one, two] = self.predict(nums, 0, len(nums) - 1, 1)
        if one >= two:
            return True
        else:
            return False

    def predict(self, nums, begin, end, player):
        if begin > end:
            return [0, 0]
        if player == 1:
            [temp_one, temp_two] = self.predict(nums, begin + 1, end, 2)
            temp_one += nums[begin]
            gap = temp_one - temp_two
            [temp_one_, temp_two_] = self.predict(nums, begin, end - 1, 2)
            temp_one_ = temp_one_ + nums[end]
            if gap > temp_one_ - temp_two_:
                player_one = temp_one
                player_two = temp_two
            else:
                player_one = temp_one_
                player_two = temp_two_
        elif player == 2:
            [temp_one, temp_two] = self.predict(nums, begin + 1, end, 1)
            temp_two += nums[begin]
            gap = temp_two - temp_one
            [temp_one_, temp_two_] = self.predict(nums, begin, end - 1, 1)
            temp_two_ += nums[end]
            if gap > temp_two_ - temp_one_:
                player_two = temp_two
                player_one = temp_one
            else:
                player_two = temp_two_
                player_one = temp_one_
        return [player_one, player_two]


if __name__ == "__main__":
    solution = Solution()
    nums = [3606449, 6]
    print(solution.PredictTheWinner(nums))
