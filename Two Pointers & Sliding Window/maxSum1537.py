'''
We must take the common elements and won't miss them;
And there will be two path between the common elements,
and we will take and only take one path.

We calculate the sum of both path, and take the bigger one.


Explanation
So we apply two points solutions,
and always take the step in the smaller element.

If two elements are the same,
we compare the accumulated sum in the both paths,
and we pick the bigger one.
'''

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        # 2 ptrs O(m + n)
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        max1, max2, res = 0, 0, 0
        while i < m or j < n:
            if i < m and (j == n or nums1[i] < nums2[j]):
                max1 += nums1[i]
                i += 1
            elif j < n and (i == m or nums1[i] > nums2[j]):
                max2 += nums2[j]
                j += 1
            else: # num1 == num2, when meet, choose bigger path
                max1 = max2 = max(max1, max2) + nums1[i]
                i += 1
                j += 1
        return max(max1, max2) % (10**9 + 7)