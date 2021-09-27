'''
you can think about it like - idx maintaining the position of where the zero appears,

Iterate through the column in reverse direction
If element is non zero, copy over where the zero appears with the non zero element
idx effectively counts number of zeros
All the elements who have been copied over ( i.e moved down ) are now filled with zero

1
0
0
2  i
0 
0  idx

1
0
0  i
2  
0  idx
2  

O(m^2n^2)/O(mn)
Worst case, everytime we only find one candy, thus we need run mn/3 times while loop, inside while loop,
it is 2mn, so total time will be m^2n^2, space will be O(mn)
'''
class Solution:
    def candyCrush(self, board):
        m,n = len(board), len(board[0])
        while True:
            # Step 1: get crush marked           
            crush = set()
            for i in range(m):
                for j in range(n):
                    if i > 1 and board[i][j] and board[i-2][j] == board[i-1][j] == board[i][j]:
                        # check board[i][j] != 0 as well !!!
                        crush |= {(i, j), (i-1, j), (i-2, j)}
                    if j > 1 and board[i][j] and board[i][j-2] == board[i][j-1] == board[i][j]:
                        crush |= {(i, j), (i, j-1), (i, j-2)}
                
            # Step 2: set crush to zero
            # print(crush)
            if not crush:
                break
            for x, y in crush:
                board[x][y] = 0
            
            # Step 3: drop
            for j in range(n):
                # check col by col (j)
                idx = m - 1 # idx of zero, to be overwritten
                # from bottom to top to prevent overwritten
                for i in range(m - 1, -1, -1):
                    # i: fast pt, idx: slow pt
                    if board[i][j]:
                        # set zero to the first non-zero
                        board[idx][j] = board[i][j]
                        idx -= 1
                
                for i in range(idx + 1):
                    board[i][j] = 0  # set top part to zero 
            
        return board


board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
m, n = len(board), len(board[0])

print('---- before ----')
print(board)

soln = Solution()
soln.candyCrush(board)

print('---- after ----')
print(board)



'''

def drop(board):
    # Step 3: drop
    for j in range(n):
        # check col by col (j)
        idx = m - 1 # idx of zero, to be overwritten
        # from bottom to top to prevent overwritten
        for i in range(m - 1, -1, -1):
            # print(i, board, idx)
            if board[i][j]:
                # set zero to the first non-zero
                board[idx][j] = board[i][j]
                idx -= 1
            print(board, i, idx)
        
        print(board, i, idx)
        print('----')
        for i in range(idx + 1):
            board[i][j] = 0   


drop(board)
print('final:', board)

'''