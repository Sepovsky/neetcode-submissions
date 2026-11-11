# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        idx = 0
        stack = [root]
        
        for val in preorder[1:]:
            node = TreeNode(val)

            if stack[-1].val != inorder[idx]:
                stack[-1].left = node
            
            else:
                while stack and stack[-1].val == inorder[idx]:
                    parent = stack.pop()
                    idx += 1
                
                parent.right = node
            
            stack.append(node)
        return root


        
        # def dfs(pre, ino):
        #     if not pre:
        #         return None
        #     root = TreeNode(pre[0])
        #     idx = ino.index(pre[0])

        #     root.left = dfs(pre[1:idx + 1], ino[:idx])
        #     root.right = dfs(pre[idx+1:], ino[idx + 1:])

        #     return root


        
        