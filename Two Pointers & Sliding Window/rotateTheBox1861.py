class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            i = len(row) - 1 # start from the bottom, i is index for settling(slow one)
            for j in range(len(row) - 1, -1, -1):
                if row[j] == '*':
                    i = j - 1 # find a new bottom, set to the left of the boundary
                elif row[j] == '#':
                    row[j], row[i] = row[i], row[j]
                    i -= 1
        # print(box, box[::-1])   
        return zip(*(box[::-1]))