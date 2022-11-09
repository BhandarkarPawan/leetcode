#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#

# @lc code=start
from collections import defaultdict, deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        adjacency = defaultdict(lambda: set())
        inCount = defaultdict(lambda: 0)

        if not prerequisites:
            return True

        for p, q in prerequisites:
            adjacency[p].add(q)
            inCount[q] += 1
            if p not in inCount:
                inCount[p] = 0

        queue = deque()
        for p, q in inCount.items():
            if q == 0:
                queue.append(p)

        res = []
        while queue:
            parent = queue.popleft()
            res.append(parent)
            children = adjacency[parent]

            for c in children:
                inCount[c] -= 1
                if inCount[c] == 0:
                    queue.append(c)

        return len(res) == len(inCount)
# @lc code=end
