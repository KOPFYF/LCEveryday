class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        inv_cnt = defaultdict(list)
        for k,v in cnt.items():
            inv_cnt[v].append(k)
        # print(cnt, inv_cnt)
        freqs = sorted(inv_cnt.keys(), reverse=True)
        res = []
        for v in freqs:
            for k in inv_cnt[v]:
                # print(v, k)
                res += k * v
        return ''.join(res)