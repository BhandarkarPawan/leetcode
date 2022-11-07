#
# @lc app=leetcode id=1465 lang=python
#
# [1465] Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
#

# @lc code=start
class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """

        sortedH = sorted(horizontalCuts)
        sortedV = sorted(verticalCuts)

        maxH = 0
        lastHCut = 0

        for hCut in sortedH:
            maxH = max(maxH, hCut - lastHCut)
            lastHCut = hCut
        maxH = max(maxH, h-lastHCut)

        maxV = 0
        lastVCut = 0
        for vCut in sortedV:
            print(vCut, lastVCut)
            maxV = max(maxV, vCut - lastVCut)
            lastVCut = vCut
        maxV = max(maxV, w-lastVCut)

        return int((maxH * maxV) % 1000000007)

# @lc code=end
