#
# @lc app=leetcode id=73 lang=python
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        rows_to_zero = set()
        cols_to_zero = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)

        for i in range(m):
            for j in range(n):
                if i in rows_to_zero or j in cols_to_zero:
                    matrix[i][j] = 0


# @lc code=end
