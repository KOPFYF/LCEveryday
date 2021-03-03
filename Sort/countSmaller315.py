class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def divide(tupn):
            if len(tupn) == 1:
                return tupn
            mid = len(tupn) // 2
            left = divide(tupn[:mid])
            right = divide(tupn[mid:])
            return conquer(left, right)
        
        def conquer(left, right):
            sor = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i][0] > right[j][0]:
                    sor.append(left[i])
                    res[left[i][1]] += len(right) - j
                    i += 1
                else:
                    sor.append(right[j])
                    j += 1
            sor.extend(left[i:] or right[j:])
            return sor
        
        if not nums:
            return []
        res = [0] * len(nums)
        tupn = [(n,i) for i,n in enumerate(nums)]
        divide(tupn)
        return res
    
        # merge sort
        def sort(indexes):
            half = len(indexes) // 2
            if half:
                left, right = sort(indexes[:half]), sort(indexes[half:])
                for i in range(len(indexes))[::-1]:
                    if not right or left and nums[left[-1]] > nums[right[-1]]:
                        smaller[left[-1]] += len(right)
                        indexes[i] = left.pop()
                    else:
                        indexes[i] = right.pop()
            return indexes
        smaller = [0] * len(nums)
        sort(range(len(nums)))
        return smaller