class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        '''
        P[i] = P[j] - P[i+1] = P[k] - P[j+1] = P[-1] - P[k+1]
        --- i --- j --- k ---- end
        '''
        # O(n^3)/O(n)
        presum = [0]
        n = len(nums)
        for num in nums:
            presum.append(presum[-1] + num)
            
        dic = defaultdict(list)
        for i, s in enumerate(presum):
            dic[s].append(i)
            
        for j in range(1, n - 1):
            for k in range(j + 2, n - 1):
                for i in dic[presum[-1] - presum[k+1]]:
                    if i + 1 >= j:
                        break
                    if i != 0 and presum[i] == presum[j] - presum[i+1] == presum[k] - presum[j+1]:
                        return True
        return False

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