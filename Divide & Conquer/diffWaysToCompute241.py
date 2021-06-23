class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        @lru_cache(None)
        def dfs(expression):
            # return a list of numbers(int) for a subarray
            if expression.isdigit():
                return [int(expression)]
            
            res = []
            for i, ch in enumerate(expression):
                if ch in "+-*/":
                    # divide & conquer
                    l, r = dfs(expression[:i]), dfs(expression[i+1:])
                    res += [eval(str(x) + ch + str(y)) for x in l for y in r]
            return res
        
        return dfs(expression)