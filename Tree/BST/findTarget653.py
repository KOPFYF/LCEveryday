class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root: 
            return False

        # BFS with seen set, O(n)/O(n) 
        dq, seen = deque([root]), set()
        while dq:
            cur = dq.popleft()
            if k - cur.val in seen: 
                return True
            seen.add(cur.val)
            if cur.left: 
                dq.append(cur.left)
            if cur.right: 
                dq.append(cur.right) 
        return False


class Solution1:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # inorder traverse
        self.s = []
        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            self.s.append(node.val)
            dfs(node.right)
        
        dfs(root)
        # print(self.s)
        l, r = 0, len(self.s) - 1
        while l < r:
            if self.s[l] + self.s[r] == k:
                return True
            elif self.s[l] + self.s[r] < k:
                l += 1
            else:
                r -= 1
        return False