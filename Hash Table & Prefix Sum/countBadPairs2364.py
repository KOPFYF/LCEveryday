'''
j - i != nums[j] - nums[i]

nums[j] - j != nums[i] - i
[4,1,3,3]
[0,1,2,3]

[4,0,1,0]

'''
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # O(n) / O(n)
        nums2 = [num - i for i, num in enumerate(nums)]
        
        dic = defaultdict(int)
        for i, num in enumerate(nums2):
            dic[num] += 1
        
        res = len(nums) * (len(nums) - 1) // 2
        for val, cnt in dic.items():
            res -= cnt * (cnt - 1) // 2
            
        return res