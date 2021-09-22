'''
Create an N-by-N matrix grid, with all elements initialized with value N.
Reset those elements to 0 whose positions are in the mines list.
For each position (i, j), find the maximum length of 1's in each of the four directions and set grid[i][j] to the minimum of these four lengths. Note that there is a simple recurrence relation relating the maximum length of 1's at current position with previous position for each of the four directions (labeled as l, r, u, d).
Loop through the grid matrix and choose the maximum element which will be the largest axis-aligned plus sign of 1's contained in the grid.

N = 5, mines = [[4,2]]

               ----j--->
               <---k----
5 5 5 5 5      1 2 3 2 1 | ^      1 1 3 2 1      1 1 1 2 1      1 1 1 1 1     1 1 1 1 1
5 5 5 5 5      2 . . . . | |      1 2 3 2 1      1 2 2 2 1      1 2 2 2 1     1 2 2 2 1
5 5 5 5 5 ---> 3 . . . . j k ---> 3 3 . . . ---> 1 2 2 2 1 ---> 1 2 2 2 1 --> 1 2 2 2 1
5 5 5 5 5      2 . . . . | |      2 2 . . .      2 2 1 . .      2 2 1 2 1     2 2 1 2 1
5 5 0 5 5      1 . 0 . . v |      1 1 0 . .      1 1 0 . .      1 1 0 1 .     1 1 0 1 1

  START        #1: i = 0          #2: i = 1      #3: i = 2      #4: i = 3     #5: i = 4
'''
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # DP, O(n^2)/O(n^2)
        dp = [[n] * n for _ in range(n)]
        for r, c in mines:
            dp[r][c] = 0
        for i in range(n):
            l, r, t, b = 0, 0, 0, 0
            for j, k in zip(range(n), reversed(range(n))):
                l = 0 if dp[i][j] == 0 else l + 1
                dp[i][j] = min(dp[i][j], l)
                r = 0 if dp[i][k] == 0 else r + 1
                dp[i][k] = min(dp[i][k], r)
                t = 0 if dp[j][i] == 0 else t + 1
                dp[j][i] = min(dp[j][i], t)
                b = 0 if dp[k][i] == 0 else b + 1
                dp[k][i] = min(dp[k][i], b)
        return max(map(max, dp))
    
        