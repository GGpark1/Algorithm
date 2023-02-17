# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self):
        self.dic = {}
        self.position = 0
        self.count = 0

    def hasCycle(self, head):
        self.count += 1
        if head:
            if head not in self.dic:
                self.position += 1
                self.dic[head] = self.position
                return True if True in [self.hasCycle(head.next)] else False
            else:
                if self.dic[head] < self.count:
                    return True
                else:
                    return False
        else:
            return False