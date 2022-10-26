# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.currentMax = ""

        for i in range(len(s)):
            self.checkLongestMiddleOutPalindrome(s, i, i)
            if i > 0 and s[i] == s[i-1]:
                self.checkLongestMiddleOutPalindrome(s, i-1, i)

        return self.currentMax

    def checkLongestMiddleOutPalindrome(self, s, left, right):

        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                return

            if (right - left + 1) > len(self.currentMax):
                self.currentMax = s[left: right + 1]

            left -= 1
            right += 1
