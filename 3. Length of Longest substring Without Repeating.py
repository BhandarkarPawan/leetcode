class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        end = 0

        counts = {}
        res = 0

        while end < len(s):
            char = s[end]
            while char in counts and start < end:
                sChar = s[start]
                counts[sChar] -= 1
                if counts[sChar] == 0:
                    del counts[sChar]
                start = start + 1

            counts[char] = 1
            res = max(res, end-start+1)
            end = end + 1

        return res
