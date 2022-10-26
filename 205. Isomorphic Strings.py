# https: // leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}

        for a, b in zip(s, t):
            if a in smap:
                if smap[a] != b:
                    return False
            if b in tmap:
                if tmap[b] != a:
                    return False
            else:
                smap[a] = b
                tmap[b] = a

        return True
