class Solution:
    def isThree(self, n: int) -> bool:
        if n == 1: return False # edge case 
        
        x = int(sqrt(n))
        if x*x != n: return False 
        
        for i in range(2, int(sqrt(x))+1): 
            if x % i == 0: 
                return False 
        return True
    
    
        cnt = 0
        for i in range(2, n):
            if n % i == 0:
                cnt += 1
                if cnt > 1:
                    return False
        return cnt == 1