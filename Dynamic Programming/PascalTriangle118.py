class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        num = [[1], [1, 1]]
        if numRows == 1:
            return [num[0]]
        elif numRows == 2:
            return num
        elif numRows == 0:
            return []
        
        row = []
        for i in range(2, numRows):
            for j in range(i - 1):
                row.append(sum(num[-1][j:j + 2]))
            num.append([1] + row + [1])
            row = []

        return num


class Solution2:
        def generate(self, numRows):
            #    1 3 3 1 0 
            # +  0 1 3 3 1
            # =  1 4 6 4 1
            res = [[1]]
            for i in range(1, numRows):
                res += [map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])]
            return res[:numRows]


 # Pascal's Triangle II
 class Solution:
    def getRow(self, numRows: int) -> List[int]:
            res = [1]
            if numRows == 0:
                return res
            for i in range(1, numRows + 1):
                res = list(map(lambda x, y: x + y, res + [0], [0] + res))
            return res