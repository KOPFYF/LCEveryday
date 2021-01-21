# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # reverse preorder traversal, like a bottom up
        self.prev = None
        def helper(root):
            if not root: return []
            helper(root.right)
            helper(root.left)
            
            root.right = self.prev # 
            root.left = None
            self.prev = root
            
        helper(root)
        
'''
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37154/8-lines-of-python-solution-(reverse-preorder-traversal)
    root
    / 
  1 
 / \\ 
3  4  
Let's see what is happening with this code.

Node(4).right = None
Node(4).left = None
prev = Node(4)

Node(3).right = Node(4) (prev)
Node(3).left = None
prev = Node(3)->Node(4)

Node(1).right = prev = Node(3) -> Node(4)
Node(1).left = None
prev = Node(1)->Node(3)->Node(4) (Which is the answer)

The answer use self.prev to recode the ordered tree of the right part of current node.
Remove the left part of current node

'''
        
            