class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:  

        def dfs(i: int = 0, path: str = '', value: int = 0, prev: int = 0):
            if i == len(num) and value == target:
                res.append(path)
                return

            for j in range(i + 1, len(num) + 1):
                string = num[i:j]
                number = int(string)
                if len(string) > 1 and num[i] == '0': 
                # if string != '0' and num[i] == '0': 
                    continue # prevent "00*"('05', '01', etc) as a number
                if not path:
                    dfs(j, string, number, number) # no prev operation
                else: # '+', '-', or '*'
                    dfs(j, path + '+' + string, value + number, number)
                    dfs(j, path + '-' + string, value - number, -number)
                    # if multipy, undo last step to reverse it's effect 
                    dfs(j, path + '*' + string, value - prev + prev * number, prev * number)

        res = []
        dfs()
        return res