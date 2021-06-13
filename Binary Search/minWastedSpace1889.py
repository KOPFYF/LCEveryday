class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        # BS, O(sort(A) + sort(B) + BlogA) / O(sort)
        # for each box in box[i] from small to big,
        # find out how many packages in A it can covers
        mod, res = 10**9 + 7, float('inf')
        packages.sort()
        
        for box in boxes:
            box.sort()
            if box[-1] < packages[-1]: 
                # check if the largest box from this supplier can hold the largest package
                # if not, we just move on to the next supplier
                continue
            cur, i = 0, 0
            for b in box:
                # Assume we alreay cover i packages,
                # now we find that we can cover j packages,
                # the space we are using (j - i) * box size.
                j = bisect.bisect(packages, b, i) # bisect start from index i
                cur += b * (j - i)
                i = j # move pointer to next package, one package in each box
            res = min(res, cur)
        
        return (res - sum(packages)) % mod if res != float('inf') else -1 