# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: #Checking if both nodes are same then return true
            return True
        if p is None or q is None: # Checking One node is empty, the other isn't. Not a match!      
            return False
        if p.val!= q.val: # Checking values are matching or not
            return False 

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)