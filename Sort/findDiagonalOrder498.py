class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # O(mn)/O(mn)
        d = defaultdict(list)
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                d[i+j].append(num)
        
        res = []
        for k, v in d.items():
            if k % 2 == 0: # reverse
                res += v[::-1]
            else:
                res += v
        return res
                