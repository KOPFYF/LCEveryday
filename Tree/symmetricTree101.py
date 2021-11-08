# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # BFS check pair by pair
        q = collections.deque([root.left, root.right])
        
        while q:
            t1, t2 = q.popleft(), q.popleft()
            if not t1 and not t2:
                continue
            elif (not t1 or not t2) or (t1.val != t2.val):
                return False
            q += [t1.left, t2.right, t1.right, t2.left]
            
        return True
    
        def dfs(node1, node2):
            # return True if the subtree is Symmetric
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            
            if node1.val == node2.val:
                outPair = dfs(node1.left, node2.right)
                inPair = dfs(node1.right, node2.left)
                return outPair and inPair
            else:
                return False
            
        return dfs(root, root)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
