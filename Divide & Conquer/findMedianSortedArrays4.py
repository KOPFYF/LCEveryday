class Solution0:
    def findMedianSortedArrays(self, nums1, nums2):
        # 2 pointers
        m, n = len(nums1), len(nums2)
        flag = 1 if (m+n)&1 == 1 else 0
        mid = (m+n)//2
        l1 = l2 = count = 0
        L = []
        while l1<m and l2<n and count<=mid:
            if nums1[l1]>nums2[l2]:
                L.append(nums2[l2])
                l2 += 1
            else:
                L.append(nums1[l1])
                l1 += 1
            count += 1
        while l1<m and count <=mid:
            L.append(nums1[l1])
            l1 += 1
            count += 1
        while l2<n and count <= mid:
            L.append(nums2[l2])
            l2 += 1
            count += 1
        return L[mid]/1. if flag else (L[mid]+L[mid-1])/2.



class Solution:
    # No slicing
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def find(self, nums1, s1, e1, nums2, s2, e2, k):
        if e1 - s1 < 0:
            return nums2[k + s2]
        if e2 - s2 < 0:
            return nums1[k + s1]
        if k < 1:
            return min(nums1[k + s1], nums2[k + s2])
        ia, ib = (s1 + e1) // 2 , (s2 + e2) // 2
        ma, mb = nums1[ia], nums2[ib]
        if (ia - s1) + (ib - s2) < k:
            if ma > mb:
                return self.find(nums1, s1, e1, nums2, ib + 1, e2, k - (ib - s2) - 1)
            else:
                return self.find(nums1, ia + 1, e1, nums2, s2, e2, k - (ia - s1) - 1)
        else:
            if ma > mb:
                return self.find(nums1, s1, ia - 1, nums2, s2, e2, k)
            else:
                return self.find(nums1, s1, e1, nums2, s2, ib - 1, k)

    def findMedianSortedArrays(self, nums1, nums2):
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.find(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, l // 2)
        else:
            return (self.find(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, l // 2) + \
                    self.find(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, l // 2 - 1)) / 2.0






class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # divide and conquer
        m, n = len(nums1), len(nums2)
        l = m + n
        if l % 2:
            return self.kthlargest(nums1, nums2, l // 2)
        else:
            return (self.kthlargest(nums1, nums2, l // 2) + self.kthlargest(nums1, nums2, l // 2 - 1)) / 2
        
    def kthlargest(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        
        l1, l2 = len(nums1) // 2, len(nums2) // 2
        median1, median2 = nums1[l1], nums2[l2]
        
        # when k is bigger than the sum of a and b's median indices 
        if l1 + l2 < k:
            # if nums1's median is bigger than nums2's, 
            # then nums2's first half doesn't include k
            if median1 > median2: # take all median2 left
                return self.kthlargest(nums1, nums2[l2 + 1:], k - l2 - 1)
            else:
                return self.kthlargest(nums1[l1 + 1:], nums2, k - l1 - 1)
        else:
            # if nums1's median is bigger than nums2's, 
            # then nums1's second half doesn't include k
            if median1 > median2: 
                return self.kthlargest(nums1[:l1], nums2, k)
            else:
                return self.kthlargest(nums1, nums2[:l2], k)