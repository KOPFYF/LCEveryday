# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # heap, O(nlogn)
        if not root: return []
        heap = []
        def helper(root, x, y):
            if not root: return 
            heapq.heappush(heap, (y, x, root.val))
            helper(root.left, x+1, y-1)
            helper(root.right, x+1, y+1)
        
        helper(root, 0, 0)
        # print(heap)
        res = []
        pre_y = -inf
        while heap:
            y, x, val = heapq.heappop(heap)
            if y == pre_y:
                res[-1] += [val]
            else:
                res.append([val])
            pre_y = y      
        return res 
    
		# BFS + sort
		dic = collections.defaultdict(list)
		queue = [(root,0,0)]
		ans = []
		while queue:
			for _ in range(len(queue)):
				node, hd, vd = queue.pop(0)
				dic[hd].append((vd, node.val))
				if node.left:
					queue.append((node.left, hd-1, vd-1))
				if node.right:
					queue.append((node.right, hd+1, vd-1))
		for i in sorted(dic.keys()):
			level = [x[1] for x in sorted(dic[i], key=lambda x:(-x[0], x[1]))]   
			ans.append(level)
		return ans
    
        # DFS + sort, O(nlogn)
        if not root: return []
        dic = defaultdict(list)
        
        def helper(root, x, y):
            if not root: return 
            dic[(x, y)].append(root.val)
            helper(root.left, x+1, y-1)
            helper(root.right, x+1, y+1)
        
        helper(root, 0, 0)
        position = sorted(dic, key = lambda x: (x[1], x[0]))
        res = []
        pre_y = -inf
        for x, y in position:
            if y == pre_y:
                res[-1].extend(sorted(dic[x, y]))
            else:
                res.append(sorted(dic[x, y]))
            pre_y = y      
        return res    