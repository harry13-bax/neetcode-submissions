# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        from collections import deque
        if root is None:
            return 0
        queue=deque([root])
        result=[]
        while queue:
            node=queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            result.append(node.val)
        result.sort()
        return result[k-1]



        