#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        m = len(matrix)
        n = len(matrix[0])

        res = []

        topmostProcessedRow = -1
        bottommostProcessedRow = m
        rightMostProcessedColumn = n
        leftMostProcessedColumn = -1

        dir = "row_right"
        fixed_index = 0
        dir_start = 0
        dir_end = n
        dir_step = 1

        while len(res) < m * n:
            for i in range(dir_start, dir_end, dir_step):
                if (dir in ["row_right", "row_left"]):
                    res.append(matrix[fixed_index][i])
                else:
                    res.append(matrix[i][fixed_index])

            if (dir == "row_right"):
                dir = "col_down"
                topmostProcessedRow += 1
                fixed_index = rightMostProcessedColumn - 1
                dir_start = topmostProcessedRow + 1
                dir_end = bottommostProcessedRow
                dir_step = 1

            elif (dir == "col_down"):
                dir = "row_left"
                rightMostProcessedColumn -= 1
                fixed_index = bottommostProcessedRow - 1
                dir_start = rightMostProcessedColumn - 1
                dir_end = leftMostProcessedColumn
                dir_step = -1

            elif (dir == "row_left"):
                dir = "col_up"
                bottommostProcessedRow -= 1
                fixed_index = leftMostProcessedColumn + 1
                dir_start = bottommostProcessedRow - 1
                dir_end = topmostProcessedRow
                dir_step = -1

            else:
                dir = "row_right"
                leftMostProcessedColumn += 1
                fixed_index = topmostProcessedRow + 1
                dir_start = leftMostProcessedColumn + 1
                dir_end = rightMostProcessedColumn
                dir_step = 1

        return res


# @lc code=end
