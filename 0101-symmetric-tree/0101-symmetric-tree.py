# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        return self.isSame(root.left, root.right)

    def isSame(self, rootleft, rootright):
        if rootleft == None and rootright == None:
            return True
        elif rootleft == None or rootright == None:
            return False
        elif rootleft.val != rootright.val:
            return False
        elif rootleft.val == rootright.val:
            return self.isSame(rootleft.left, rootright.right) and self.isSame(rootleft.right, rootright.left)