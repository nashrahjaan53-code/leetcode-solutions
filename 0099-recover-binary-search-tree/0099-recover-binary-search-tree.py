class Solution:
    def recoverTree(self, root):
        

       
        stack = []
        first = None
        second = None
        prev = None
        current = root
        
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            

            if prev and prev.val > current.val:
                if not first:
                    first = prev
                second = current
            
            prev = current
            current = current.right
        

        if first and second:
            first.val, second.val = second.val, first.val











        