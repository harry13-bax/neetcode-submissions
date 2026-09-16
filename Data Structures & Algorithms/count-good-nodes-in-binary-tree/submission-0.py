# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        if root is None:
            return 0
        def calc(root,maxi):
            nonlocal count
            if root.val>=maxi:
                count+=1
            maxi=max(maxi,root.val)
            if root.left:
                calc(root.left,maxi)
            if root.right:
                calc(root.right,maxi)
        calc(root,root.val)
        return count
            
        