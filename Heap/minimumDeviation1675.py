class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:   
        # heap
        def find_bound(n):
            # return (lower bound, upper bound)
            # 11 => (11, 22), 10 => (5, 10), 8 => (1, 8)
            if n % 2:
                n *= 2
            cur = n
            while cur % 2 == 0:
                cur //= 2
            return cur, n
        
        nums = [(l, r) for l, r in map(find_bound, nums)] # all possible combinations 
        # print(nums) # [(1, 2), (1, 2), (3, 6), (1, 4)]
        heapq.heapify(nums)
        upper, lower = max(a[0] for a in nums), min(a[0] for a in nums) # 3, 1
        res = upper - lower # 2
        
        while nums[0][0] < nums[0][1]:
            l, r = heapq.heappop(nums)
            heapq.heappush(nums, (l * 2, r)) # multiply the odd value by 2
            upper = max(upper, l * 2)
            lower = nums[0][0]
            res = min(res, upper - lower)
            # print(l, r, upper, lower, res)
            # print(nums) # final state [(2, 2), (2, 2), (3, 6), (2, 4)]
        return res
            
        
        
        
        # minimize the max diff
        hq = []
        for num in nums:
            cur = num
            while cur % 2 == 0:
                cur //= 2
            # put in pair (num, limit), 
            # 3 => (3, 6), 12 => (3, 12)
            hq.append((cur, max(num, cur * 2))) # now hq size is n
        
        maxm = max(num for num, limit in hq)
        res = float('inf')
        heapq.heapify(hq)
        
        while len(hq) == len(nums):
            num, limit = heapq.heappop(hq)
            res = min(res, maxm - num)
            if num < limit:
                heapq.heappush(hq, (num*2, limit))
                maxm = max(maxm, num*2)
        
        return res
        
            