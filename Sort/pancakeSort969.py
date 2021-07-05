class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # bubble sort O(n^2)
        # Find the index i of the next maximum number x.
        # Reverse i + 1 numbers, so that the x will be at A[0]
        # Reverse x numbers, so that x will be at A[x - 1].
        # Repeat this process N times.
        # (a b x) (c d)
        # _  _  i  _ _
        # (x b a) (c d)
        # d c a b x
        res = []
        n = len(A)
        for x in range(n, 1, -1):
            i = A.index(x)
            A[:i+1] = A[:i+1][::-1]
            res.append(i + 1)
            A = A[::-1][:-1]
            res.append(x)
        return res
        
        
        res = []
        for x in range(len(A), 1, -1):
            # print(len(A))
            i = A.index(x)
            res.extend([i + 1, x])
            # A = A[:i:-1] + A[:i]
            A = A[i+1:][::-1] + A[:i]
        return res
    
        res = []
        done = 0
        while sorted(A) != A:
            lstToCheck = A[0:len(A) - done]
            indOfLargest = A.index(max(lstToCheck))
            if indOfLargest != 0:
                res.append(indOfLargest + 1)
            res.append(len(A) - done)
            A = A[:indOfLargest + 1][::-1] + A[indOfLargest + 1:]
            A[:len(A) - done] = A[:len(A) - done][::-1]
            done += 1
        return res