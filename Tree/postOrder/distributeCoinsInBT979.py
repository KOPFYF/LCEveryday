# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        # postOrder, traverses the tree bottom up
        self.res = 0
        def postOrder(root):
            if not root:
                return 0
            left, right = postOrder(root.left), postOrder(root.right)
            self.res += abs(left) + abs(right) # accumulate the abs value of traffic
            # keep one coin for the root, return the sum
            return root.val + left + right - 1
        
        postOrder(root)
        return self.res


class Solution2:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # the child give x=(y-1) coins to parent, if he has y coins
        # post order
        def dfs(node, parent):
            # return moves we need for current node
            if not node:
                return 0
            moves = dfs(node.left, node) + dfs(node.right, node)
            if parent:
                parent.val += (node.val - 1)
            # if y=0=> x=-1 then parent should give the child 1 coin
            moves += abs(node.val - 1)
            return moves

        return dfs(root, None)