'''
  i  
                   -
    -     -   -
  -   - -   - 
- 
      l   r
      
concat left of left and right of right

1 2 3 10 4 2 3 5
      l    r
'''
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n - 1
        
        while l < n - 1 and arr[l] <= arr[l+1]:
            l += 1
        if l == n - 1: 
            return 0
        while r >= l and arr[r-1] <= arr[r]:
            r -= 1
        if r == 0:
            return n - 1
        
        res = min(n - l - 1, r) # to remove
        i, j = 0, r
        while i <= l and j < n:
            # print(res, i, j, j - i)
            if arr[j] >= arr[i]:
                res = min(res, j - i - 1)
                i += 1
            else:
                j += 1
        return res
 
        # for loop, same
        for i in range(l + 1):
            if arr[i] <= arr[r]:
                res = min(res, r - i - 1)
            elif arr[i] > arr[r] and r < n - 1:
                r += 1
            else:
                print(r) # r = n - 1
                break
        return res
            
            