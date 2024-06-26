# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def depth(node):
            if not node:
                return 0
            l, r = depth(node.left), depth(node.right)
            return 1 + max(l, r)
        
        height = depth(root) # number of rows = height + 1
        width = 2 ** height - 1
        res = [[''] * width for i in range(height)]
        # print(height, width, res) # 2 3 [['', '', ''], ['', '', '']]
        
        def dfs(node, r, c):
            res[r][c] = str(node.val)
            if node.left:
                dfs(node.left, r + 1, c - 2**(height - r - 2)) # height
            if node.right:
                dfs(node.right, r + 1, c + 2**(height - r - 2))
        
        dfs(root, 0, width >> 1)
        return res


class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def get_height(node):
            return 0 if not node else 1 + max(get_height(node.left), get_height(node.right))
        
        def update_output(node, row, left, right):
            if not node:
                return
            mid = (left + right) // 2
            self.output[row][mid] = str(node.val)
            update_output(node.left, row + 1 , left, mid - 1)
            update_output(node.right, row + 1 , mid + 1, right)
            
        height = get_height(root)
        width = 2 ** height - 1
        self.output = [[''] * width for i in range(height)]
        update_output(node=root, row=0, left=0, right=width - 1)
        return self.output