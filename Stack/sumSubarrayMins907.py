class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # find vally pattern (k --- j --- i)
        res, s = 0, []
        # add 2 ends so dont need i - j + 1, even subarray is like [3]
        arr = [0] + arr + [0] 
        for i, a in enumerate(arr):
            while s and arr[s[-1]] > a:
                j = s.pop()
                k = s[-1]
                res += arr[j] * (i - j) * (j - k)
            s.append(i)
        return res % (10**9 + 7)


class Solution2:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # Combine mono inc stack(left) & mono inc stack(right)
        # current num is a valley
        n, mod = len(arr), 10**9 + 7
        left, right, s1, s2 = [-1] * n, [-1] * n, [], []
        for i, a1 in enumerate(arr):
            while s1 and arr[s1[-1]] > a1:
                s1.pop()
            left[i] = i - s1[-1] if s1 else i + 1
            s1.append(i)
        
        for i, a2 in enumerate(arr):
            while s2 and arr[s2[-1]] > a2:
                right[s2.pop()] = i
            s2.append(i)
        for i in range(n):
            right[i] = n - i if right[i] == -1 else right[i] - i
            
        return sum(a * l * r for a, l, r in zip(arr, left, right)) % mod