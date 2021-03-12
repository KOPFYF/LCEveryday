class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.d = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.d[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        res = 0
        for j, v in vec.d.items():
            if j in self.d:
                res += v * self.d[j]
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)