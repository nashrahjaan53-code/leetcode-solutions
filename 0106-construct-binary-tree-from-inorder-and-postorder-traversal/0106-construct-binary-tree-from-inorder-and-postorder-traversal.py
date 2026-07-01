class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        mid = inorder.index(root_val)
        
        root.right = self.buildTree(inorder[mid+1:], postorder)
        root.left = self.buildTree(inorder[:mid], postorder)
        
        return root












        