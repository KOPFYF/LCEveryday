class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        m, n = len(word), len(abbr)
        
        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == '0':
                return False # leading 0
            elif abbr[j].isdigit():
                k = j
                while k < n and abbr[k].isdigit():
                    k += 1
                cnt = int(abbr[j:k])
                # jump i & j with the count
                i += cnt
                j = k
            else: # unmatched
                return False
            
            
        return i == m and j == n