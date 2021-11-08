# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        '''
        The level-order traversal array of a complete binary tree will never have a null node in between non-null nodes. If we encounter a null node, all the following nodes should also be null, otherwise it's not complete.
        '''
        
        if not root:
            return True
        q = collections.deque([(root, 1)])
        res = []
        while q:
            u, coord = q.popleft()
            res.append(coord)
            if u.left:
                q.append((u.left, 2 * coord))
            if u.right:
                q.append((u.right, 2 * coord + 1))
        print(res) 
        # [1, 2, 3, 4, 5, 6] True 6 == 6
        # [1, 2, 3, 4, 5, 7] False 7 != 6
        return len(res) == res[-1]
    
        has_null = False
        bfs = deque([root])
        while bfs:
            node = bfs.popleft()
            if not node:
                has_null = True
                continue
            if has_null:
                return False
            bfs.append(node.left)
            bfs.append(node.right)
        
        # print(bfs) 
        return True