#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start


class Solution:
    def combinationSum(self, candidates, target: int):
        candidates = sorted(candidates)
        self.ans = []
        self.sub_sum(candidates, target, [])
        return self.ans

    def sub_sum(self, candidates: list, target: int, path: list):
        for i in range(len(candidates)):
            value = target - candidates[i]
            if value == 0:
                tmp = path + [candidates[i]]
                self.ans.append(tmp)
            elif value < 0:
                continue
            elif value > 0:
                tmp = path + [candidates[i]]
                self.sub_sum(candidates[i:], value, tmp)


# @lc code=end
