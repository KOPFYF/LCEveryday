class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        # reduce, find patterns
        intervals = []
        len_windows = set([len(word) for word in words])
        words = set(words)
        n = len(s)
        for l in len_windows:
            for i in range(n - l + 1):
                if s[i:i+l] in words:
                    intervals.append([i, i+l])
        
        # merge intervals
        intervals.sort()
        merged = []
        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            elif merged[-1][1] >= start and merged[-1][1] < end:
                # overlapped
                merged[-1][1] = end
        
        # print(merged)
        res, prev_end = "", 0
        for start, end in merged:
            res += s[prev_end:start] + '<b>' + s[start:end] + '</b>'
            prev_end = end
        return res + s[prev_end:]