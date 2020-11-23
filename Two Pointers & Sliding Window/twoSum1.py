class Solution_hash(object):
    def twoSum(self, nums, target):
    	# time O(n), space O(n)
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


    def twoSum2(self, nums, target):
    	# easier to understand
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i


class Solution_2pts(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(nlogn)
        nums2 = sorted(nums)
        l,r = 0, len(nums)-1
        while l < r:
            tmp = nums2[l] + nums2[r]
            if tmp > target:
                r -= 1
            elif tmp < target:
                l += 1
            else:
                a, b = nums2[l], nums2[r]
                break

        res = []
        for i in range(len(nums)):
            if nums[i] == a:
                res.append(i)
                break
                
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == b:
                res.append(i)
                break
        return res