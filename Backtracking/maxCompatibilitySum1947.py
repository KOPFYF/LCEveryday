class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
#         # TLE
#         m, n = len(students), len(students[0])
#         def dot_prod(a, b): # O(n)
#             res = 0
#             for x, y in zip(a, b):
#                 res += int(x == y)
#             # print(a, b, res)
#             return res

        
#         res = 0
#         for scomb in permutations(students):
#             for mcomb in permutations(mentors):
#                 cur = 0
#                 for student, mentor in zip(scomb, mcomb):
#                     cur += dot(student, mentor)
#                 res = max(cur, res)
#         return res

        pair_score = defaultdict(int)
        n = len(students)

        # build compatibilty score for every possible student-mentor pair
        for i in range(n):
            for j in range(n):
                pair_score[i, j] = sum(s_ans == m_ans for s_ans, m_ans in zip(students[i], mentors[j]))
        
        # try to pair student[i] with every unused mentor
        # mentor[j] is unused if 'j'th bit in mask is '1'
        @cache
        def dfs(i, mask):
            if i == len(students):
                return 0
            return max(dfs(i + 1, mask ^ (1 << j)) + pair_score[i, j] for j in range(n) if (1 << j) & mask)
                    
        return dfs(0, (1 << n) - 1)
    
    
        self.score = 0
        m = len(students)
        men = set()

        def dfs(i, cur):
            if i == m:
                self.score = max(self.score, cur)
                return
            for j in range(m):
                if j not in men:
                    tmp = 0
                    for k in range(len(students[i])):
                        tmp += students[i][k] == mentors[j][k]
                    men.add(j)
                    cur += tmp
                    dfs(i + 1, cur)
                    cur -= tmp
                    men.remove(j)
        dfs(0, 0)
        return self.score