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
        # pre:  root-left-right
        # post: left-right-root
        # soln 0(bug)
        if post:
            root = TreeNode(pre.pop(0))
            if len(post) > 1:
                i = post.index(pre[0])
                root.left = self.constructFromPrePost(pre, post[:i])
                root.right = self.constructFromPrePost(pre, post[i:-1])
            return root
        
        # soln 1
        # https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/discuss/748216/Python3-Solution-with-a-Detailed-Explanation-Construct-Binary-Tree-from
        if pre:
            root = TreeNode(post.pop())
            if len(pre) > 1:
                i = pre.index(post[-1])
                root.right = self.constructFromPrePost(pre[i:], post)
                root.left = self.constructFromPrePost(pre[1:i], post)
            return root
        
        # soln 2
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