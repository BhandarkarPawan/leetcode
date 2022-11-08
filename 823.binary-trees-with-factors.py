#
# @lc app=leetcode id=823 lang=python
#
# [823] Binary Trees With Factors
#

# @lc code=start
class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        unique = set(arr)
        arr = sorted(arr)
        subTreeCounts = {}

        for v in arr:
            vCount = 1
            for op1 in subTreeCounts:
                if v % op1 == 0:
                    op2 = v // op1
                    if op2 in subTreeCounts:
                        vCount += subTreeCounts[op1] * subTreeCounts[op2]
            subTreeCounts[v] = vCount

        return int(sum(subTreeCounts.values()) % (1e+9 + 7))

# @lc code=end
