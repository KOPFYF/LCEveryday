class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.cnt = 0
        self.res = None
        def helper(root):
            if root:
                helper(root.left)
                self.cnt += 1
                if self.cnt == k:
                    self.res = root.val
                    return
                helper(root.right)
        
        helper(root)
        return self.res


class Solution2(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        def helper(root, res):
            if root:
                helper(root.left, res)
                res.append(root.val)
                helper(root.right, res)
        
        helper(root, res)
        return res[k - 1]