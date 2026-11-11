# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        
        stack = []
        ctr = 0
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            ctr += 1
            if ctr == k:
                return curr.val
            
            curr = curr.right

            


        
