# https://leetcode.com/problems/first-bad-version/
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while (left < right):
            mid = (left + right)//2
            if isBadVersion(mid):
                # Either mid or something before mid is bad
                # right = mid
            else:
                # the earliest would be after mid
                # left = mid + 1

        return left
