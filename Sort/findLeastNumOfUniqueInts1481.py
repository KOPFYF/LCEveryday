class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # O(n) / O(n)
        c = Counter(arr)
        cnt, remaining = Counter(c.values()), len(c)
        # print(c, cnt, cnt[3]) # [5,5,4] : (Counter({5: 2, 4: 1}), Counter({1: 1, 2: 1}))
        for key in range(1, len(arr) + 1): 
            if k >= key * cnt[key]:
                k -= key * cnt[key]
                remaining -= cnt[key]
            else:
                return remaining - k // key
        return remaining
    
        # O(nlogn) / O(n)
        d = Counter(arr)
        c = list(d.values())
        c.sort(reverse=True)
        while k > 0:
            k -= c.pop()
        return len(c) if k >= 0 else len(c) + 1