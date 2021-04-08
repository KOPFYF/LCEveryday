class Solution:
    def maximizeSweetness(self, nums: List[int], K: int) -> int:
        # k = K + 1
        def check(target):
            # return True if you can split into k+1 items and min < (target)
            runsum, cuts = 0, 0
            for num in nums:
                runsum += num
                if runsum > target:
                    cuts += 1
                    runsum = 0
                    if cuts > K:
                        return False
            return True
        
        l, r = 1, sum(nums)
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l