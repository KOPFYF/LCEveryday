'''
In order to rotate clockwise, first reverse rows order, then transpose the matrix;
Rotate 0, 1, 2, 3 times and compare the rotated matrix with target, respectively.

Some explanation, suppose we are at index i, j, let us find a relation of this position with it's position in various rotations
i. e
0deg rotation : i, j will point to i, j
90deg rotation : i, j will point to j, n - i - 1
180deg rotation : i, j will point to n - i - 1, n - j - 1
270deg rotation : i, j will point to n - j - 1, i

We denote these rotations by boolean variables, initially we assume all these rotations are valid, so we set them all to true
here c[0] denotes 0deg rotation, c[1] -> 90deg, c[2] -> 180 deg, c[3] -> 270deg

Then, we loop over all elements and check if that particular rotation is valid or not. If not, we turn it to false.
In the end, we simply check if any of the rotations is still possible or not.

This same code can also be used to find out the valid rotation, i,e 0deg / 90deg / 180 deg/ 270 deg by checking the boolean value in c[0], c[1]. c[2], c[3] respectively.
'''
class Solution0:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        res = [True] * 4
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]: 
                    # 0deg rotation : i, j will point to i, j
                    res[0] = False
                if mat[i][j] != target[n-j-1][i]: 
                    # 90deg rotation : i, j will point to j, n - i - 1
                    res[1] = False
                if mat[i][j] != target[n-i-1][n-j-1]: 
                    # 180deg rotation : i, j will point to n - i - 1, n - j - 1
                    res[2] = False
                if mat[i][j] != target[j][n-i-1]:
                    # 270deg rotation : i, j will point to n - j - 1, i
                    res[3] = False
        return any(res)

# https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
class Solution1:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            # mat = [list(x) for x in zip(*mat[::-1])]
            mat = [list(x[::-1]) for x in zip(*mat)]
        return False


