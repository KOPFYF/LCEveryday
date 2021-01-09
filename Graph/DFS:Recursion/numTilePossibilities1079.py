class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        res = set()
        def dfs(path, t):
            if path not in res:
                if path:
                    res.add(path)
                for i in range(len(t)):
                    # make sure each char is used once in each path
                    dfs(path + t[i], t[:i] + t[i + 1:])
                
        dfs('', tiles)
        return len(res)