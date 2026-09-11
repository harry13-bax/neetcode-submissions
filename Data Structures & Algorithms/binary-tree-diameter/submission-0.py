# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        di=0
        def height(root):
            nonlocal di
            if root is None:
                return 0
            l=height(root.left)
            r=height(root.right)
            di=max(di,l+r)
            return 1+max(l,r)
        height(root)
        return di



        