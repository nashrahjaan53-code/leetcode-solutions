class Solution:
    def isValidBST(self, root):
        if not root:
            return True
        
        stack = []
        prev = float('-inf')
        current = root
        
        while stack or current:

            while current:
                stack.append(current)
                current = current.left
            

            current = stack.pop()
            

            if current.val <= prev:
                return False
            prev = current.val
            

            current = current.right
        
        return True











        