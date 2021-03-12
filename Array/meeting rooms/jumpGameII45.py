class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """       
        
        # implicit bfs solution
        # the range of the current jump is [curBegin, curEnd] ? 
        # curFarthest is the farthest point that all points in [curBegin, curEnd] 
        if len(nums) <= 1: return 0
        jumps, curend, curfarthest = 0, 0, 0
        for i in range(len(nums) - 1): # why -1??
            curfarthest = max(curfarthest, i + nums[i])
            if i == curend:
                jumps += 1
                curend = curfarthest
        return jumps
        
        # O(n) greedy
        if len(nums) <= 1: return 0
        # min intervals
        end1, end2, cnt = -1, 0, 0
        for i in range(len(nums)):
            if end1 < i:
                cnt += 1
                end1 = end2
            end2 = max(end2, nums[i] + i)
            # print(i, end1, end2, cnt)
            # [2,3,1,1,4]
            # (0, 0, 2, 1)
            # (1, 2, 4, 2)

            if end2 >= len(nums) - 1:
                return cnt
        
        
        
        
        # Same as 763. Partition Labels
        if len(nums) <= 1: return 0
        res = 1
        l, r = 0, nums[0]
        
        while r < len(nums) - 1:
            res += 1
            nxt = max(i + nums[i] for i in range(l, r+1))
            l, r = r, nxt
        
        return res