class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        nums = [x*x*a + x*b + c for x in nums]
        res = [0] * len(nums)
        l, r = 0, len(nums) - 1
        if a < 0:
            i, d = l, 1 # start from left, fill 2 ends first
        else:
            i, d = r, -1 # start from right, reverse fill
            
        while l <= r:
            if nums[l] * -d > nums[r] * -d:
                res[i] = nums[l]
                l += 1
            else:
                res[i] = nums[r]
                r -= 1
            i += d
        return res
        
        
        # Math + Two Pointers
        def quadratic(x):
            return a*x*x + b*x + c 
        n = len(nums)
        index = 0 if a < 0 else n-1
        l, r, ans = 0, n-1, [0] * n
        while l <= r:
            l_val, r_val = quadratic(nums[l]), quadratic(nums[r])
            if a >= 0:
                if l_val > r_val:
                    ans[index] = l_val 
                    l += 1
                else:    
                    ans[index] = r_val 
                    r -= 1
                index -= 1
            else:
                if l_val > r_val:
                    ans[index] = r_val 
                    r -= 1
                else:    
                    ans[index] = l_val 
                    l += 1
                index += 1
        return ans
        
        # sort O(nlogn)
        nums2 = [a*x*x + b*x + c for x in nums]
        nums2.sort()
        
        return nums2