class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # soln 1, binary search to find left bound, O(logn)
        l, r = 0, len(arr) - k
        while l < r:
            m = (l + r) // 2
            if x - arr[m] > arr[m+k] - x: 
                # keep a sliding window and compare 2 ends
                l = m + 1
            else:
                r = m
        return arr[l:l+k]


class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:        
        # soln 2, sliding win + binary search, 
        if len(arr) == k:
            return arr
        
        left = bisect_left(arr, x) - 1
        right = left + 1

        while right - left - 1 < k:
            # Be careful to not go out of bounds
            if left == -1:
                right += 1
                continue
            
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        return arr[left + 1:right]
    
        
class Solution3:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:    
        # soln3, O(nlogk)
        hq = []
        for a in arr:
            heapq.heappush(hq, (-abs(a - x), -a))
            if len(hq) > k:
                heapq.heappop(hq)
        
        res = [-x for _, x in hq]
        return sorted(res)
    
        