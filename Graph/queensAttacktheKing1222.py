class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # 0 <= queens[i][j] < 8
        res = []
        queens = set((i, j) for i, j in queens)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for k in range(1, 8):
                    x, y = king[0] + dx * k, king[1] + dy * k
                    if (x, y) in queens:
                        res.append([x, y])
                        break # only 1 candidate in each direction
        return res
                    