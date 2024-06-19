no# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # BFS
        if not root: return []

        table = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, index = queue.popleft()
            table[index].append(node.val)
            if node.left:
                queue.append((node.left, index-1))
            if node.right:
                queue.append((node.right, index+1))
        # The keys of the table are the indices, if we sort them we get from lowest to highest index
        # return [table[index] for index in sorted(table)]

        # no need to sort
        return [table[i] for i in range(min(table), max(table) + 1)]