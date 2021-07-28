class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # Rotate the box using the relation rotatedBox[i][j] = box[m - 1 - j][i].
        # Start iterating from the bottom of the box and for each empty cell check if there is any stone above it with no obstacles between them.

        for row in box:
            i = len(row) - 1
            for j in range(len(row) - 1, -1, -1):
                if row[j] == '*':
                    i = j - 1 # bottom position, below is obstacle
                elif row[j] == '#':
                    row[j], row[i] = row[i], row[j]
                    i -= 1
        
        return zip(*(box[::-1]))