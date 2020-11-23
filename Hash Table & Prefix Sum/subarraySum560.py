class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1
        prefix_sum, res = 0, 0
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in hashmap:
                res += hashmap[prefix_sum - k]
            hashmap[prefix_sum] += 1
        return res