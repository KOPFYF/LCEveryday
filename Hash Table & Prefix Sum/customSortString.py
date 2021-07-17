class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # hash table O(n)/O(n)
        # Return any permutation of s that satisfies this property.
        # Corner case: ch in s but not in order, then put it in the end
        cnt = collections.Counter(s)
        res = ""
        # sort chars both in order and s by the order of order.
        for ch in order:
            if ch in cnt:
                res += cnt[ch] * ch
                del cnt[ch] # remove sorted
        for k, v in cnt.items():
            res += k * v
        return res