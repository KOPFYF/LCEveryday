'''
Consider how many nodes are in the nth level down of a binary tree:

n = 1: 1 = 2^0
n = 2: 2 = 2^1
n = 3: 4 = 2^2

The pattern is that the nth level down will have 2 ^ (n - 1) nodes in it.

Now consider how many nodes are in a tree of height h. It will be the sum of all levels. So if the height is h, it will be:

2^0 + 2^1 + ... + 2^(h - 1). This equals 2^h - 1 (https://en.wikipedia.org/wiki/1_%2B_2_%2B_4_%2B_8_%2B_⋯#Summation).

The representation of the tree needs to have one column for each node in a full tree of the given tree's height, according to the rules given, so the width will need to be 2^h - 1.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def getHeight(node):
            if not node:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        def dfs(node, row, l, r):
            if not node:
                return
            mid = (l + r) // 2
            self.res[row][mid] = str(node.val)
            dfs(node.left, row + 1, l, mid - 1)
            dfs(node.right, row + 1, mid + 1, r)
            
        height = getHeight(root) # number of rows, actually it's height + 1
        width = 2 ** height - 1
        # print(height, width)
        self.res = [[''] * width for _ in range(height)]
        dfs(root, 0, 0, width - 1)
        return self.res