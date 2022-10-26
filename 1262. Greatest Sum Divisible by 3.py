# https://leetcode.com/problems/greatest-sum-divisible-by-three/
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        rem1 = []
        rem2 = []

        res = sum(nums)

        if res % 3 == 0:
            return res

        for n in nums:
            if n % 3 == 1:
                rem1.append(n)
            if n % 3 == 2:
                rem2.append(n)

        rem1.sort()
        rem2.sort()

        if res % 3 == 1:
            if len(rem2) < 2:
                if len(rem1) == 0:
                    return 0
                else:
                    return res - rem1[0]
            else:
                if len(rem1) == 0:
                    return res - sum(rem2[:2])
                else:
                    return res - min(sum(rem1[:1]), sum(rem2[:2]))

        elif res % 3 == 2:
            if len(rem1) < 2:
                if len(rem2) == 0:
                    return 0
                else:
                    return res - rem2[0]
            else:
                if len(rem2) == 0:
                    return res - sum(rem1[:2])
                else:
                    return res - min(sum(rem2[:1]), sum(rem1[:2]))

        return 0
