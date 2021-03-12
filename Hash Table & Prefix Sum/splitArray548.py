class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        '''
        0 ... i ... j ... k ... n-1
        
        '''
        n = len(nums)
        sums = [0] * (n + 1)
        for i in range(n):
            sums[i + 1] = sums[i] + nums[i]
        for j in range(3, n - 3):
            s = set()
            for i in range(1, j - 1):
                if sums[i] == (sums[j] - sums[i+1]):
                    s.add(sums[i])
            for k in range(j + 2, n - 1):
                sjk = sums[k] - sums[j+1]
                skn = sums[n] - sums[k+1]
                if sjk == skn and sjk in s:
                    return True
        return False