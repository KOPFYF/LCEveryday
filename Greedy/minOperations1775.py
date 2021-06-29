class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        # O(mlogm + nlogn), heap
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2 * 6 or n2 > n1 * 6:
            return -1
        
        s1, s2 = sum(nums1), sum(nums2)
        if s1 > s2: # make sure s1 <= s2, and convert s1 to s2
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1
            
        hq1, hq2 = [], []
        for num1 in nums1:
            heapq.heappush(hq1, num1) # min heap, pop out min
        for num2 in nums2:
            heapq.heappush(hq2, -num2) # max heap, pop out max
            
        res = 0
        while s1 < s2:
            res += 1
            if len(hq2) == 0 or -hq2[0] - 1 < 6 - hq1[0]:
                # greedily use min(hq1), move it to 6
                s1 += 6 - heapq.heappop(hq1)
            else:
                s2 -= (-heapq.heappop(hq2) - 1)
        return res
        
        
        # O(n)
        N = len(nums1)
        M = len(nums2)
        s1 = sum(nums1)
        s2 = sum(nums2)
        if N > 6*M or M > 6*N:
            return -1
        elif s1 == s2:
            return 0
        else:
            c1 = collections.Counter(nums1)
            c2 = collections.Counter(nums2)
            if s2 > s1:
                s1, s2 = s2, s1
                c1, c2 = c2, c1
            res = 0
            dif = abs(s1-s2)
            for i in range(6):
                ct = c1[6-i] + c2[1+i]
                val = 5-i
                if val*ct < dif:
                    dif -= val*ct
                    res += ct
                elif val*ct >= dif:
                    ct = math.ceil(dif/val)
                    dif -= val*ct
                    res += ct
                if dif <= 0:
                    return res
                
                
        # sort + 2 ptrs        
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        diff = abs(sum1 - sum2)
        if sum1 < sum2:
            nums1, nums2 = nums2, nums1
        res = 0
        nums1.sort(reverse = True)
        nums2.sort()
        i, j, m, n = 0, 0, len(nums1), len(nums2)
        while i < m or j < n:
            if not diff:
                break
            if i < m and j < n:
                if nums1[i] - 1 >= 6 - nums2[j]:
                    if diff > nums1[i] - 1:
                        diff -= nums1[i] - 1
                        res += 1
                    else:
                        diff = 0
                        res += 1
                    i += 1
                else:
                    if diff > 6 - nums2[j]:
                        diff -= 6 - nums2[j]
                        res += 1
                    else:
                        diff = 0
                        res += 1
                    j += 1
            elif i < m:
                if diff > nums1[i] - 1:
                    diff -= nums1[i] - 1
                    res += 1
                else:
                    diff = 0
                    res += 1
                i += 1
            else:
                if diff > 6 - nums2[j]:
                    diff -= 6 - nums2[j]
                    res += 1
                else:
                    diff = 0
                    res += 1
                j += 1
        return res if not diff else -1
        

        
        
            
            
        
        