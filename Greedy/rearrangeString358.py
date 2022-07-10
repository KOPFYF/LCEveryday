class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if not k: 
            return s
        n = len(s)
        cnts = Counter(s)
        freqs = list(cnts.values())
        max_n = max(freqs)
        max_f = freqs.count(max_n)
        tmp = (max_n - 1) * k + max_f

        if tmp > n:
            return ""
        
        res = list(s)
        i = (n - 1) % k # init from begining
        # print(i)
        for c in sorted(cnts, key=lambda i: -cnts[i]):
            # print(res)
            for _ in range(cnts[c]):
                # print(i)
                res[i] = c
                i += k
                if i >= n: # start from beginning
                    i = (i - 1) % k
        # print(res)
        return "".join(res)