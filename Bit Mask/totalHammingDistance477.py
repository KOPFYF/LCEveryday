class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        if not nums: return 0
        bit_count, n, res = defaultdict(int), len(nums), 0
        for num in nums:
            i = 0
            while num:
                if num & 1: # count 1
                    bit_count[i] += 1 # hashmap to store counts of 1
                num >>= 1
                i += 1
        
        for cnt in bit_count.values():
            res += cnt * (n - cnt)
        return res