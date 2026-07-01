# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and 
                    isMirror(left.left, right.right) and 
                    isMirror(left.right, right.left))
        
        return isMirror(root.left, root.right)
    
    def isSymmetricIterative(self, root):
        if not root:
            return True
        
        queue = [(root.left, root.right)]
        
        while queue:
            left, right = queue.pop(0)
            
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        
        return True






        