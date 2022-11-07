#
# @lc app=leetcode id=811 lang=python
#
# [811] Subdomain Visit Count
#

# @lc code=start
from collections import defaultdict


class Solution(object):
    def subdomainVisits(self, cpdomains):
        hashmap = defaultdict(lambda: 0)

        res = []
        for cpdomain in cpdomains:
            rep, domain = cpdomain.split(" ")
            rep = int(rep)

            splits = domain.split(".")

            hashmap[domain] += rep
            topLevel = splits[-1]
            hashmap[topLevel] += rep

            if len(splits) == 3:
                midLevel = f"{splits[1]}.{splits[2]}"
                hashmap[midLevel] += rep

        for key, value in hashmap.items():
            res.append(f"{value} {key}")

        return res
# @lc code=end
