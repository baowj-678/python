# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

#  

# 示例 1：

# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：

# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  

# 限制：

# 0 <= matrix.length <= 100
# 0 <= matrix[i].length <= 100

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def spiralOrder(self, matrix):
        if(len(matrix) == 0):
            return []
        CONSTANT = -9999
        height = len(matrix)
        width = len(matrix[0])
        length = height * width
        out = [0] * length
        i = 0
        x, y = 0, 0
        direct = 0
        while(i < length):
            print(x, y)
            out[i] = matrix[x][y]
            i += 1
            matrix[x][y] = CONSTANT
            if(direct == 0):
                if(y + 1 < width and matrix[x][y + 1] != CONSTANT):
                    y += 1
                    continue
                else:
                    direct = 1
                    x += 1
                    matrix
                    continue
            if(direct == 1):
                if(x + 1 < height and matrix[x + 1][y] != CONSTANT):
                    x += 1
                    continue
                else:
                    direct = 2
                    y -= 1
                    continue
            if(direct == 2):
                if(y > 0 and matrix[x][y - 1] != CONSTANT):
                    y -= 1
                    continue
                else:
                    direct = 3
                    x -= 1
                    continue
            if(direct == 3):
                if(x > 0 and matrix[x - 1][y] != CONSTANT):
                    x -= 1
                    continue
                else:
                    direct = 0
                    y += 1
                    continue
        return out


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3]]
    print(s.spiralOrder(matrix))
