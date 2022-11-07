#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start
from collections import defaultdict


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        grid_map = defaultdict(lambda: set())

        n = len(board)

        for i in range(n):
            row_set = set({})
            col_set = set({})
            for j in range(n):
                row_val = board[i][j]
                col_val = board[j][i]
                grid_key = i * 10 + j

                if row_val != "." and row_val in row_set:
                    return False

                if col_val != "." and col_val in col_set:
                    return False

                row_set.add(row_val)
                col_set.add(col_val)

                if row_val in grid_map[grid_key]:
                    return False

                grid_map[grid_key].add(row_val)

        return True


# @lc code=end
