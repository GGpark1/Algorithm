class Solution:

    def __init__(self):
        self.list = []
        self.count = 0

    def GetNodeList(self, head):
        if head:
            self.list.append(head)
            self.GetNodeList(head.next)
        else:
            return self.list


    def getIntersectionNode(self, headA, headB):
        self.GetNodeList(headA)
        first_set = set(self.list)

        while headB not in first_set:
            if headB is None:
                return None

            headB = headB.next

        return headB