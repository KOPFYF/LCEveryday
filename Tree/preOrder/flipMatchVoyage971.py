class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.pos = 0
        res = []
        
        def dfs(node, voyage):
            if not node:
                return True
            if node.val != voyage[self.pos]:
                return False
            self.pos += 1
            
            if dfs(node.left, voyage) and dfs(node.right, voyage):
                return True
            
            # flip and retry
            res.append(node.val)
            return dfs(node.right, voyage) and dfs(node.left, voyage)
        
            # node.left, node.right = node.right, node.left
            # res.append(node.val)
            # return dfs(node.left, voyage) and dfs(node.right, voyage)
        
        if not dfs(root, voyage):
            return [-1]
        return res