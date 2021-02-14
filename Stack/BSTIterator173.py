# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = [] # store directed left children from root.
        self.pushAll(root)

    def next(self) -> int:
        node = self.stack.pop()
        self.pushAll(node.right)
        return node.val
        
    def hasNext(self) -> bool:
        return bool(self.stack)
    
    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left