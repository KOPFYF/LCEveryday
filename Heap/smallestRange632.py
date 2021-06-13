class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        hq = [(x[0], i, 0) for i, x in enumerate(nums)]
        heapq.heapify(hq) # Keep a heap of the smallest elements
        
        res = [-float('inf'), float('inf')]
        upper = max(x[0] for x in nums)
        while hq:
            lower, i, j = heapq.heappop(hq)
            if upper - lower < res[1] - res[0]:
                res = [lower, upper]
            if j + 1 == len(nums[i]): 
                # any row to the end, since we cannot abandon this row, has to return
                return res
            upper = max(upper, nums[i][j + 1])
            heapq.heappush(hq, (nums[i][j + 1], i, j + 1))