class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # sort + dict, O(mn + klogk + [::-1])
        d = defaultdict(list)
        for i, row in enumerate(nums):
            for j, num in enumerate(row):
                d[i+j].append(num) 
        res = []
        for k in sorted(d.keys()):
            res += d[k][::-1] # reverse the order
        return res
        
        # sort, O(mn + mnlogmn) / O(mn)
        # numbers with equal sums of row and column indexes belong to the same diagonal.
        flatten = []
        for i, row in enumerate(nums):
            for j, num in enumerate(row):
                flatten.append((i+j, -i, num)) # (sum, row, val)
        flatten.sort()
        
        return [x[2] for x in flatten]