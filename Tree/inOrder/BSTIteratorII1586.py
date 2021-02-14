# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.arr = self.inOrder(root)
        self.idx = -1

    def hasNext(self) -> bool:
        return self.idx + 1 < len(self.arr)

    def next(self) -> int:
        self.idx += 1
        return self.arr[self.idx]

    def hasPrev(self) -> bool:
        return self.idx >= 1
        
    def prev(self) -> int:
        self.idx -= 1
        return self.arr[self.idx]     
        
    def inOrder(self, node):
        if node:
            return self.inOrder(node.left) + [node.val] + self.inOrder(node.right)
        else:
            return []