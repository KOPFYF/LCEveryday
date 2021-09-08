class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        '''
        O(8**n) --> as there are 8 branches at each step and I can go max of n depth
        '''
        deadlock = {(1,3):2, (1,7):4, (1,9):5, (2,8):5, (3,7):5, (3,1):2, (3,9):6, (4,6):5, (6,4):5, (7,1):4, (7,3):5, (7,9):8, (8,2):5, (9,7):8, (9,3):6, (9,1):5}
        # print(len(deadlock)) # 16, (3 rows + 3 cols + 2 diags) * 2
        self.res = 0
        
        def dfs(num, cnt, m, n, seen):
            # number of combs with length between m and n, starting from num
            if m <= cnt <= n:
                self.res += 1
            if cnt == n:
                return
            seen.add(num)
            for nxt_num in range(1, 10):
                if nxt_num in seen:
                    continue
                if (num, nxt_num) in deadlock and deadlock[(num, nxt_num)] not in seen:
                    # case 1: passes through the center 
                    # case 2: center previously appeared
                    continue
                dfs(nxt_num, cnt + 1, m, n, seen)
            seen.remove(num)
                
        
        for num in range(1, 10):
            seen = set()
            dfs(num, 1, m, n, seen)
        return self.res
            
