#
# @lc app=leetcode id=48 lang=python
#
# [48] Rotate Image
#

# @lc code=start
from audioop import reverse


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            matrix[i] = reversed(matrix[i])

# @lc code=end
