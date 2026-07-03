class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        

        cloned = {}
        
        def dfs(original):
            if original in cloned:
                return cloned[original]
            

            copy = Node(original.val)
            cloned[original] = copy
            

            for neighbor in original.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node)


 










        