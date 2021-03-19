class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # 2 pointers, O (n^2)
        # nums[i] + nums[j] + nums[k] < target
        nums.sort() # order does not matter
        cnt, n = 0, len(nums)
        for i, num in enumerate(nums[:-2]):
            if num * 3 > target:
                return cnt
            j, k = i + 1, n - 1
            while j < k: # fix i and find j ~ k
                if num + nums[j] + nums[k] < target:
                    cnt += k - j
                    j += 1
                else:
                    k -= 1
        return cnt