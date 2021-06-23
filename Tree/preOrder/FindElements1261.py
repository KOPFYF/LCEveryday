# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        # hashmap
        self.root = root
        self.root.val = 0
        self.d = defaultdict(int)
        self.dfs(self.root)
        
    def dfs(self, root):
        if not root:
            return
        x = root.val
        self.d[x] += 1
        if root.left:
            root.left.val = 2 * x + 1
            self.dfs(root.left)
        if root.right:
            root.right.val = 2 * x + 2
            self.dfs(root.right)
        
    def find(self, target: int) -> bool:
        return self.d[target] > 0


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)