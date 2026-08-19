# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:#no root node
            return 0
        #leaf nodes
        if not root.left and not root.right:
            return 1
        #if no left child exists
        if not root.left:
            return 1+self.minDepth(root.right)
        #if right child doesnt exists
        if not root.right:
            return 1+self.minDepth(root.left)
        #both child exists
        return 1+min(self.minDepth(root.left),self.minDepth(root.right))
