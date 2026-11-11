# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        qp = deque([p])
        qq = deque([q])

        while qp and qq:
            pnode = qp.popleft()
            qnode = qq.popleft()

            if not pnode and not qnode:
                continue

            if not pnode or not qnode:
                return False
                
            if pnode.val != qnode.val:
                return False
            
            qp.append(pnode.left)
            qp.append(pnode.right)
            
            qq.append(qnode.left)
            qq.append(qnode.right)
        
        return True


        