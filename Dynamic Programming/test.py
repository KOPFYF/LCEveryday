class SolutionTest:
    def minInsertions(self, s: str) -> int:
        self.count = 0
        def dfs(i, j):
            self.count += 1
            print(self.count)
            if j - i < 1:
                return 0
            if s[i] == s[j]:
                return dfs(i + 1, j - 1)
            else:
                return min(dfs(i + 1, j), dfs(i, j - 1)) + 1

        return dfs(0, len(s) - 1)

s = "abcdef"
a = SolutionTest()
print(a.minInsertions(s))