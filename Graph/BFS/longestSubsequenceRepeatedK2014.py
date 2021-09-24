class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        '''
        2 <= n < k * 8 => subsequence cannot be longer than 7 chars
        
        '''
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
        
        cands = [chr(i + 97) for i, v in enumerate(freq) if v >= k]
        # print(freq)
        # print(cands) # ['e', 'l', 't'], candidate is sorted inc, so bfs will output lexicographically largest
        
        def is_subseq(ss):
            """Return True if ss is a k-repeated sub-sequence of s."""
            i, cnt = 0, 0
            for ch in s:
                if ss[i] == ch:
                    i += 1
                    if i == len(ss):
                        cnt += 1
                        if cnt == k:
                            return True
                        i = 0
            return False
        
        res = ""
        bfs = deque([""])
        while bfs:
            ch = bfs.popleft()
            for cand in cands:
                nxt_ch = ch + cand
                if is_subseq(nxt_ch):
                    res = nxt_ch # res will be longer and longer
                    # print(res) # ete is also valid but smaller
                    bfs.append(nxt_ch)
            # print(bfs) # each time bfs len+1
        return res