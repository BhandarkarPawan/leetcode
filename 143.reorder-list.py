#
# @lc app=leetcode id=143 lang=python
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        s = head

        # find mid of linkedList
        i = head
        j = head

        # find middle of linked list
        while (j and j.next):
            i = i.next
            j = j.next.next

        # reverse the second half of linked list
        prev = None
        while (i):
            next_i = i.next
            i.next = prev
            prev = i
            i = next_i

        i = prev
        while (i and s.next != i):

            next_i = i.next
            next_s = s.next

            s.next = i
            i.next = next_s

            s = next_s
            i = next_i

        return head
# @lc code=end
