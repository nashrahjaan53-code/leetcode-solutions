class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        
        memo = {}
        
        def build_trees(start, end):
            if start > end:
                return [None]
            
            key = (start, end)
            if key in memo:
                return memo[key]
            
            result = []
            
            for root_val in range(start, end + 1):
                left_trees = build_trees(start, root_val - 1)
                right_trees = build_trees(root_val + 1, end)
                
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        result.append(root)
            
            memo[key] = result
            return result
        
        return build_trees(1, n)












        