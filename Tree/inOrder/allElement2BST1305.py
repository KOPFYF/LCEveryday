# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        arr1, arr2 = [], []
        self.inorder(root1, arr1)
        self.inorder(root2, arr2)
        n1, n2 = len(arr1), len(arr2)
        i, j = 0, 0
        res = []
        while i < n1 and j < n2:
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        while i < n1:
            res.append(arr1[i])
            i += 1
        while j < n2:
            res.append(arr2[j])
            j += 1
        return res

    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)