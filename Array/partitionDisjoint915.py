'''
need:
max(left) <= min(right)
lmax <= right(A[i])
lmax > current A[i]

'''
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        A = nums
        # 1 pass, use one more variable leftmax to moniter
        lmax, allmax, res = nums[0], nums[0], 1
        for i in range(len(A)):
            allmax = max(allmax, A[i])
            if lmax > A[i]: # satisfied for now
                res = i + 1
                lmax = allmax
        return res
                
        
        # 2 pass, skip the first maxleft pass, keep only the minright array, and use maxleft as a variable
        minright = [A[-1]]*len(A)
        for i in range(len(A)-2,-1,-1):
            minright[i] = min(minright[i+1], A[i])
            
        maxleft = A[0]
        for i in range(len(A)-1):
            maxleft = max(maxleft, A[i])  
            if maxleft <= minright[i+1]:
                return i+1
        # 3 pass
        maxleft = [A[0]]*len(A)
        for i in range(1,len(A)):
            maxleft[i] = max(maxleft[i-1], A[i])

        minright = [A[-1]]*len(A)
        for i in range(len(A)-2,-1,-1):
            minright[i] = min(minright[i+1], A[i]) 

        for i in range(len(A)-1):
            if maxleft[i] <= minright[i+1]:
                return i+1
        
        # max(left) <= min(right), 2 <= nums.length <= 30000
        # O(n) / O(1)
        lmax, allmax = nums[0], nums[0]
        res = 1
        for i in range(1, len(nums)):
            # print(nums[i], lmax, allmax, res)
            if nums[i] < lmax: # potential solution
                res = i + 1
                lmax = allmax
            else:
                allmax = max(allmax, nums[i])
        return res
        