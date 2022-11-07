#
# @lc app=leetcode id=622 lang=python
#
# [622] Design Circular Queue
#

# @lc code=start
class MyCircularQueue(object):

    def __init__(self, k: int):
        self.k = k
        self.queue = [-1] * self.k
        self.front = 0
        self.rear = -1
        self.curLen = 0

    def enQueue(self, value: int) -> bool:
        if self.curLen == self.k:
            return False

        self.rear = (self.rear + 1) % self.k
        self.queue[self.rear] = value
        self.curLen += 1
        return True

    def deQueue(self) -> bool:
        if self.curLen == 0:
            return False

        self.front = (self.front + 1) % self.k
        self.curLen -= 1
        return True

    def Front(self) -> int:
        if self.curLen == 0:
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.curLen == 0:
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.curLen == 0

    def isFull(self) -> bool:
        return self.curLen == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end
