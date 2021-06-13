class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        vals = sorted(list(c.keys()), reverse=True)
        # print(c, vals)
        ops = 0
        for largest, nextLargest in zip(vals, vals[1:]):
            ops += c[largest]
            c[nextLargest] += c[largest]
        return ops