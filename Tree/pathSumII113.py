# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # DFS
        if not root:
            return []
        res = []
        self.dfs(root, sum, [], res)
        return res

    def dfs(self, root, target, ls, res):
        if root:
            if not root.left and not root.right and target == root.val:
                ls += [root.val]
                res.append(ls)
            if root.left:
                self.dfs(root.left, target - root.val, ls + [root.val], res)
            if root.right:
                self.dfs(root.right, target - root.val, ls + [root.val], res)

class Solution1:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []
        res = []
        def dfs(root, target, path):
            if not root.left and not root.right and root.val == target:
                res.append(path + [root.val])
            if root.left:
                dfs(root.left, target - root.val, path + [root.val])
            if root.right:
                dfs(root.right, target - root.val, path + [root.val])
        
        dfs(root, sum, [])
        return res

class Solution2(object):
    def pathSum(self, root, sum):
        if not root:
            return []
        if not root.left and not root.right and sum == root.val:
            return [[root.val]]
        tmp = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        return [[root.val] + i for i in tmp]


class Solution3(object):
    # BFS + queue    
    def pathSum3(self, root, sum): 
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])] # current node, running sum, running path
        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == sum:
                res.append(ls)
            if curr.left:
                queue.append((curr.left, val+curr.left.val, ls+[curr.left.val]))
            if curr.right:
                queue.append((curr.right, val+curr.right.val, ls+[curr.right.val]))
        return res


class Solution4(object):
    # DFS + stack I  
    def pathSum4(self, root, sum): 
        if not root:
            return []
        res = []
        stack = [(root, sum-root.val, [root.val])] # current node, current need, running path
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, val-curr.right.val, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, val-curr.left.val, ls+[curr.left.val]))
        return res

        