class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        '''
        [2, 3, 4, 7, 11] (missing)
        [1, 2, 3, 4, 5] (no missing)
        
        '''
        # binary search O(logn)
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            if arr[mid] - mid - 1 < k:
                l = mid + 1
            else:
                r = mid
        return l + k
        
        
        # O(n)
        arr = set(arr)
        cnt = 0
        num = 1
        while True:
            if num not in arr:
                cnt += 1
                if cnt == k:
                    return num
            num += 1