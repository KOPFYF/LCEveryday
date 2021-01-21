# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        '''
        bottom-up level的顺序是：notCover层, hasCamera层，covered层，
        然后重复：notCover,hasCamera,covered,...
        解释：leaf层是notCover, leaf层上面的parent层是hasCamera层，
            parent层上面是covered层(因为parent层摄像头覆盖了本层)，而covered层上面是notCover层。
        
        covered(parent of parent, 2)
            |
        hasCamera(parent, 1)
            |
        notCover(0, leaf)
        
        DFS + Greedy + bottom up
        Set cameras on all leaves' parents, then remove all covered nodes.
        Repeat step 1 until all nodes are covered.
        Apply a recusion function dfs.
        Return 0 if it's a leaf.
        Return 1 if it's a parent of a leaf, with a camera on this node.
        Return 2 if it's coverd, without a camera on this node.

        For each node,
        if it has a child, which is leaf (node 0), then it needs camera.
        if it has a child, which is the parent of a leaf (node 1), then it's covered.

        If it needs camera, then res++ and we return 1.
        If it's covered, we return 2.
        Otherwise, we return 0.
        '''
        self.res = 0
        def dfs(root):
            if not root: 
                return 2
            l, r = dfs(root.left), dfs(root.right)
            if l == 0 or r == 0: # l, r are leaves, current is parent with camera
                self.res += 1
                return 1
            if l == 1 or r == 1: # l, r has camera
                return 2  # covered with l/r
            else:
                return 0
        return (dfs(root) == 0) + self.res
        