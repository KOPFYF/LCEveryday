class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # use a counter to count 0
        cnt, i, res = 0, 0, 0
        for j in range(len(nums)):
            if nums[j] % 2:
                k -= 1
                cnt = 0 # meet a 1, reset countet
            while k == 0:
                cnt += 1
                k += nums[i] % 2
                i += 1
            res += cnt
        return res

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # use a tmp ptr to count 0
        i, res = 0, 0
        for j in range(len(nums)):
            k -= nums[j] % 2
            if k == 0:
                res += 1
            while k < 0:
                k += nums[i] % 2
                res += k == 0
                i += 1
            tmp = i
            while res and tmp < j and not nums[tmp] % 2:
                tmp += 1
                res += 1
        return res