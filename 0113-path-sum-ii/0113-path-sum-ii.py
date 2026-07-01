class Solution:
    def pathSum(self, root, targetSum):
        result = []
        
        def dfs(node, current_sum, path):
            if not node:
                return
            
            current_sum += node.val
            path.append(node.val)
            
            if not node.left and not node.right and current_sum == targetSum:
                result.append(list(path))
            else:
                dfs(node.left, current_sum, path)
                dfs(node.right, current_sum, path)
            
            path.pop()
        
        dfs(root, 0, [])
        return result












        