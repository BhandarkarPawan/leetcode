#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#

# @lc code=start
class Solution(object):
    def exist(self, board, word):
        visited = set()

        def isWord(i, j, suffix):
            if len(suffix) == 0:
                return True

            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != suffix[0] or (i, j) in visited:
                return False

            neighbors = [
                (i+1, j),
                (i-1, j),
                (i, j+1),
                (i, j-1)
            ]

            board[i][j] = "#"
            for a, b in neighbors:
                if isWord(a, b, suffix[1:]):
                    return True

            board[i][j] = suffix[0]

            return False

        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if isWord(i, j, word):
                    return True

        return False

# @lc code=end
