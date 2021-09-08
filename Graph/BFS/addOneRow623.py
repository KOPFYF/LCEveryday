# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        
        bfs = deque([root])
        while bfs and depth > 1:
            n = len(bfs)
            depth -= 1
            for _ in range(n):
                cur = bfs.popleft()
                if cur.left:
                    bfs.append(cur.left)
                if cur.right:
                    bfs.append(cur.right)
                
                if depth == 1:
                    cur.left = TreeNode(val, cur.left, None)
                    cur.right = TreeNode(val, None, cur.right)
        return root


class Solution2:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        # case when the level is 1
        if d == 1:
            return TreeNode(v, root, None)

        dq = deque([root])
        level = 1
        while level != d - 1:
            for _ in range(len(dq)):
                curr = dq.popleft()
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
            level += 1

        for _ in range(len(dq)):
            curr = dq.popleft()

            left = curr.left
            right = curr.right

            new1 = TreeNode(v, left, None)
            new2 = TreeNode(v, None, right)

            curr.left = new1
            curr.right = new2

        return root