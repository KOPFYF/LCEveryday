class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # O(mn)/O(m+n)
        # diag top-left -> bottom-right
        # x - y = constant, using hash table to check unique
        hash_table = {}
        m, n = len(matrix), len(matrix[0])
        for x in range(m):
            for y in range(n):
                if x - y not in hash_table:
                    hash_table[x - y] = matrix[x][y]
                else:
                    if hash_table[x - y] != matrix[x][y]:
                        return False
        return True