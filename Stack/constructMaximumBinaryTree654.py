# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
If there is a number i in the middle of nums, find the biggest number on its left and right hand side, these 2 biggest numbers should be smaller than i. We call these two numbers left and right.

If you know about Decreasing Stack, you will notice that:

When you are trying to push a number i, during the process of popping elements from the stack, the last element you pop must be the left of i .
After the popping process, if there is still an element on the top of stack, this element, say top, must be bigger than i, thus i is a candidate of the right of top.
While i might not be the final right of top, consider the example below:

Example:
nums = [3,1,2], first we process 3, then we push 1, 1then becomes the candidate of right, therefore we set node(3).right = node(1). But then we process 2, start the popping process, 1 is the last element we pop, so according to Rule1 above, node(2).left = node(1). Then we push 2 to the stack, now, node(3).right = node(2). We get the correct answer!
'''
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # Mono-stack, desc, O(n)
        if not nums:
            return
        
        stack = []
        for num in nums:
            node = TreeNode(num)
            left = None
            while stack and stack[-1].val < num:
                # when new num is bigger, pop
                left = stack.pop()
            node.left = left
            if stack:
                stack[-1].right = node
            stack.append(node)
            # left = None
        return stack[0]
        