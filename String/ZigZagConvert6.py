class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # O(n)/O(numRows)
        if numRows == 1 or numRows >= len(s):
            return s
        
        L = [''] * numRows
        index, step = 0, 1
        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1 # reverse
            index += step
            # print(L)
        return ''.join(L)