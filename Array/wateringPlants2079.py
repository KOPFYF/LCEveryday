class Solution:
    def wateringPlants(self, nums: List[int], capacity: int) -> int:
        '''
          i, steps, cap, cnt
        if  0 0 3 1
        if  1 0 1 2
        else  2 4 5 2
        if  3 4 2 3  5 > 3
        '''
        n = len(nums)
        steps = 0
        cap = capacity
        cnt = 0
        # [2,2,3,3], capacity = 5
        i = 0
        while i < n:
            if cap >= nums[i]:
                cap -= nums[i]
                cnt += 1
                i += 1
            else:
                # back
                steps += cnt * 2
                cap = capacity
        return steps + cnt