#
# @lc app=leetcode id=202 lang=python
#
# [202] Happy Number
#

# @lc code=start
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visitSums = set()

        while n > 1:

            temp = n
            curSum = 0

            while temp > 0:
                digit = temp % 10
                curSum += pow(digit, 2)
                temp = temp // 10
            if curSum in visitSums:
                return False

            n = curSum
            visitSums.add(n)

            print(n)
        return True


# @lc code=end
