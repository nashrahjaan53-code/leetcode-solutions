class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        result = []
        queue = [root]
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.pop(0)
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if left_to_right:
                result.append(current_level)
            else:
                result.append(current_level[::-1])
            
            left_to_right = not left_to_right
        
        return result











        