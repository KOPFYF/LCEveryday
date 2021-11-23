# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        # soln 1, recursion, DFS
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        # soln 2, BFS, keep a queue, FIFO
        depth = 0
        # queue = [root]
        queue = deque([root])
        while queue:
            depth += 1
            # BFS deal with all cur nods in level, 精髓在于for loop
            for i in range(len(queue)):
                # pop the left most element
                # c = queue.pop(0)
                # list: pop(0), O(n),  deque:popleft(), O(1)
                c = queue.popleft()
                if c.left:
                    queue.append(c.left)
                if c.right:
                    queue.append(c.right)
            
        return depth