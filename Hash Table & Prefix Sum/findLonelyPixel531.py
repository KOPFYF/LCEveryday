class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        # O(mn)/O(n+m), 2 passes
        m, n = len(picture),len(picture[0])
        row = [0 for _ in range(m)]
        col = [0 for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row[i] += 1
                    col[j] += 1
                    
        res = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B' and row[i] == 1 and col[j] == 1:
                    res += 1
        return res


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        # O(mn)/O(1), 1 passes
        n, m = len(picture), len(picture[0])
        res = 0
        for j in range(m):
            found = False
            for i in range(n):
                if picture[i][j] == 'B':
                    if found or picture[i].count('B') != 1:
                        found = False
                        break
                    found = True
            if found:
                res += 1
        return res