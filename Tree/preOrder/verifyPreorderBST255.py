'''
https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/discuss/469009/Python-simple-stack-O(n)-for-time-and-space

Core concept: At any point, we need to figure out the lower bound for all the values yet to be seen or processed. Now how would be manage that? Visualize a BST.
Initially that lower bound is -INF.
You start pushing all the left most values into a stack. When you find preorder[i] > preorder[i-1], it indicates a right child. We now want to find the predecessor of this right child. The predecessor will serve as new lower bound.
How do we find predecessor? Keep popping till you preorder[i] > st[-1].
'''

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # O(n)/O(n)
        stack = []
        low = float('-inf')
        for x in preorder:
            # print(stack, x, low)
            if x < low:
                return False
            while stack and stack[-1] < x: # find right
                low = stack.pop()
                # print('pop', low)
            stack.append(x) # append all left < root
            
        return True
    
        # O(n)/O(1)
        # stack = preorder[:i], reuse preorder as stack
        lower = float('-inf')
        i = 0
        for x in preorder:
            if x < lower:
                return False
            while i > 0 and x > preorder[i - 1]:
                lower = preorder[i - 1]
                i -= 1
            preorder[i] = x
            i += 1
        return True
    
        
    
        
        
        