class Solution:
    def countServers(self, A: List[List[int]]) -> int:
        # Count the number of servers in each row to X
        # Count the number of servers in each col to Y
        # If X[i] + Y[j] > 2, the server at A[i][j] (if exists) communicate.
        X, Y = tuple(map(sum, A)), tuple(map(sum, zip(*A)))
        # print(X, Y)
        # X[i] >= 1, Y[j] >= 1
        # So X[i] + Y[j] > 2 equals (X[i] > 1 or Y[j] > 1)
        return sum((X[i] > 1 or Y[j] > 1) for i in range(len(A)) for j in range(len(A[0])) if A[i][j])
        
        return sum(X[i] + Y[j] > 2 for i in range(len(A)) for j in range(len(A[0])) if A[i][j])