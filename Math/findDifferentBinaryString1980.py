class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = '' 
        for i,num in enumerate(nums):
            ans += '1' if (num[i] == '0') else '0'      #ternary if else
			# ans += str(1- int(num[i]))             # Alternate: cast to string & 1-x to flip
        return ans 
        
        # backtracking O(2^n)
        # 1 <= n <= 16
        n = len(nums)
        seen = set(nums)
        
        perm = []
        def dfs(pos, path):
            if pos == n:
                perm.append(path)
                return
            dfs(pos + 1, path + '0')
            dfs(pos + 1, path + '1')
        
        dfs(0, '')
        # print(perm)
        for i in perm:
            if i not in seen:
                return i