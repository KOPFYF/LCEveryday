class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        def rev(num):
            s = str(num)
            return int(s[::-1])
        tmp = []
        for num in nums:
            tmp.append(num - rev(num))
        # print(tmp, Counter(tmp))
        
        res = 0
        count = Counter(tmp)
        for diff, cnt in count.items():
            res += (cnt - 1) * cnt // 2
        
        return res % mod