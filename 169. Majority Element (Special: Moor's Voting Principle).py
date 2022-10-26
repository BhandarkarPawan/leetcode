# https://leetcode.com/problems/majority-element/
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        majEle = nums[0]
        majCount = 1

        for x in nums[1:]:
            if x == majEle:
                majCount += 1
            else:
                majCount -= 1
                if majCount == 0:
                    majEle = x
                    majCount = 1

        return majEle
