# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = deque()
        self._inorder(root)
        
    def _inorder(self, node):
        if not node:
            return
        self._inorder(node.left)
        self.arr.append(node.val)
        self._inorder(node.right)

    def next(self) -> int:
        return self.arr.popleft()

    def hasNext(self) -> bool:
        return len(self.arr) > 0