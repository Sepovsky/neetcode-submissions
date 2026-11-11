# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(root):
            if not root:
                return
            
            swap(root.right)
            swap(root.left)
            root.left, root.right = root.right, root.left
            return root
        return swap(root)
        