class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # greedy, O(nlogn)/O(n)
        cnt = Counter(arr)
        for a in sorted(arr, key = lambda x: abs(x)):
            # greedy, start from min(abs(x))
            if cnt[a] == 0:
                continue
            if cnt[a*2] == 0:
                return False # no such 2a
            cnt[a] -= 1
            cnt[2*a] -= 1
        return True