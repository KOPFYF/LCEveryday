class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        # O(n^2 + nlogn) / O(n)
        mod = 10 ** 9 + 7
        d = Counter(A)
        nums = sorted(d.keys())
        res, n = 0, len(nums)
        for i in range(n):
            j, k = i, n - 1
            while j <= k:
                a, b, c = nums[i], nums[j], nums[k]
                if a + b + c < target:
                    j += 1
                elif a + b + c > target:
                    k -= 1
                else:
                    if i < j < k:
                        res += d[a] * d[b] * d[c]
                    elif i == j < k:
                        res += d[a] * (d[a] - 1) // 2 * d[c]
                    elif i < j == k:
                        res += d[b] * (d[b] - 1) // 2 * d[a]
                    else:
                        res += d[a] * (d[a] - 1) * (d[a] - 2) // 6
                    j += 1
                    k -= 1
        
        return res % mod