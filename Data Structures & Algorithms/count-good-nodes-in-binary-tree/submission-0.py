# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [[root, root.val]]
        good = 0
        max_val = root.val
        while stack:
            curr, cmx = stack.pop()

            if curr.val >= cmx:
                cmx = curr.val
                good += 1

            if curr.left:
                stack.append([curr.left, cmx])

            if curr.right:
                stack.append([curr.right, cmx])

        return good