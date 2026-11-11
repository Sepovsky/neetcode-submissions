# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        while True:
            if root == None:
                return TreeNode(val=val)
            
            if val < curr.val:
                if curr.left != None:
                    curr = curr.left
                else:
                    a = TreeNode(val=val)
                    curr.left = a
                    break
            
            else:
                if curr.right != None:
                    curr = curr.right
                else:
                    a = TreeNode(val=val)
                    curr.right = a
                    break
            
        return root
        