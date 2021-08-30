'''
Explanation
s1, s2 are the prefix sum, d is a hash table for index of prefix-sum difference
Record the first index of s1-s2 in d, when the same value of s1-s2 is met after the first time:
Update ans by subtract i with d[s1-s2]
For example: nums1 = [1, 0, 1, 1]; nums2 = [0, 0, 1, 1]
At index 0, we will have d[1] = 0
At index 1, diff = 1 again, we will update ans = 1 - d[1] = 1 - 0 = 1. This is because nums1[1:2] == nums2[1:2]
At index 2, diff = 1 again, ans = 2 - d[1] = 2 - 0 = 2, due to nums1[1:3] == nums2[1:3]
At index 3, diff = 1 again, ans = 3 - d[1] = 3 - 0 = 3, due to nums1[1:4] == nums2[1:4]
'''
class Solution1:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        d = {0: -1}
        ans = s1 = s2 = 0
        for i, (v1, v2) in enumerate(zip(nums1, nums2)):
            s1, s2 = s1+v1, s2+v2
            diff = s1 - s2
            if diff not in d:
                d[diff] = i
            ans = max(ans, i - d.get(diff, sys.maxsize))
        return ans


class Solution0:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        presum1, presum2 = [0], [0]
        for i in range(n):
            presum1.append(presum1[-1] + nums1[i])
            presum2.append(presum2[-1] + nums2[i])
        
        # find the same diff, like 2 sum
        d, res = {0: -1}, 0
        for i in range(n):
            diff = presum1[i+1] - presum2[i+1]
            if diff not in d:
                d[diff] = i
            else:
                res = max(res, i - d[diff])
        return res



