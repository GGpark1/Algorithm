# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        def reverseList(self, head):
            cur = ListNode()
            stack = []
            while head:
                cur = head.val
                stack.append(cur)
                cur = head.next
                head = head.next

            res = dummy = ListNode()
            while stack:
                pop_node = stack.pop()
                if pop_node == None:
                    continue
                else:
                    res.next = ListNode(pop_node)
                    res = res.next

            return dummy.next
