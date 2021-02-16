# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        # Soln 1: 2 stacks, O(logn + k)
        # https://leetcode.com/problems/closest-binary-search-tree-value-ii/discuss/70534/O(k-%2B-logn)-Python-Solution
        ans = []
        preStack = []
        sucStack = []

        while root:
            if root.val < target:
                preStack.append(root)
                root = root.right
            else:
                sucStack.append(root)
                root = root.left
                
        def getPredecessor(stack):
            if stack:
                pre = stack.pop()
                p = pre.left
                while p:
                    stack.append(p)
                    p = p.right
                return pre
            
        def getSuccessor(stack):
            if stack:
                suc = stack.pop()
                p = suc.right
                while p:
                    stack.append(p)
                    p = p.left
                return suc
        
        pre = getPredecessor(preStack)
        suc = getSuccessor(sucStack)

        while k:
            k -= 1
            if pre and not suc:
                ans.append(pre.val)
                pre = getPredecessor(preStack)
            elif not pre and suc:
                ans.append(suc.val)
                suc = getSuccessor(sucStack)
            elif pre and suc and abs(pre.val - target) <= abs(suc.val - target):
                ans.append(pre.val)
                pre = getPredecessor(preStack)
            elif pre and suc and abs(pre.val - target) >= abs(suc.val - target):
                ans.append(suc.val)
                suc = getSuccessor(sucStack)
        return ans


class Solution2(object):
    def closestKValues(self, root, target, k):        
        # Soln 2, Inorder, O(n) + O(n - k), 36 ms
        # Inorder of BST is sorted naturally
        dq = deque()
        def inOrder(root):
            if not root: return
            inOrder(root.left)
            dq.append(root.val)
            inOrder(root.right)
        inOrder(root)
        
        while len(dq) > k:
            if abs(dq[0] - target) > abs(dq[-1] - target):
                dq.popleft()
            else:
                dq.pop()
        return dq
        

class Solution3(object):
    def closestKValues(self, root, target, k):         
        # soln 3, preOrder, O(n klogk), 48 ms
        heap = []
        def preOrder(root):
            if not root: return
            if len(heap) < k:
                heapq.heappush(heap, (-abs(root.val - target), root.val))
            else:
                heapq.heappushpop(heap, (-abs(root.val - target), root.val))
            preOrder(root.left)
            preOrder(root.right)
        preOrder(root)
        return [val for _, val in heap]