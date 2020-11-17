# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        # pre:  1,(2,4,5),(3,6,7)
        # post: (4,5,2),(6,7,3),1
        if not pre or not post: 
            return None
        root = TreeNode(pre[0])
        if len(post) == 1: 
            return root
        idx = pre.index(post[-2]) # root of right subtree
        # print(post[-2], idx)
        # pre: root-left-right  [0][1:idx](cut here)[idx:]
        # post: left-right-root [:idx-1][idx-1:-1](cut here)[-1] 
        root.left = self.constructFromPrePost(pre[1: idx], post[: (idx - 1)])
        root.right = self.constructFromPrePost(pre[idx: ], post[(idx - 1): -1])
        return root