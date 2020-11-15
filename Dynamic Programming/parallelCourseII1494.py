class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        pre = [0] * n #prerequisite
        dp = [16] * (1 << n)
        for i, j in dependencies:
            pre[j - 1] ^= 1 << (i - 1)
        # print(pre) # [6, 0, 0, 1] 6 means 110, to take course 1 we need to take course 2&3
        queue = deque([(0, 0)])
        
        # Make all courses that can be studied based on the current case a list nxt_level     
        while queue:
            state, step = queue.popleft() # current state, current semester
            nxt_level = []
            for i in range(n):
                if pre[i] & state != pre[i] or (1 << i) & state:
                    # pre[i] & state != pre[i], current state cannot satisfy course i pre
                    # (1 << i) & state: current course already in state, seen this course before
                    continue
                nxt_level.append(i)
            if len(nxt_level) < k:
                for course_id in nxt_level:
                    state ^= 1 << course_id
                if state == (1 << n) - 1:
                    return step + 1
                if dp[state] > step + 1:
                    queue.append([state, step + 1])
                    dp[state] = step + 1
            # if the length is smaller than k, we will study all, or else, we can pick k of them. 
            # For example, length = 5, k=2, there 10 combinations to check
            else:
                samples = itertools.combinations(nxt_level, k) # sample k courses
                for sample in samples:
                    tmp = state
                    for course_id in list(sample):
                        tmp ^= 1 << course_id
                    if dp[tmp] > step + 1:
                        queue.append([tmp, step + 1])
                        dp[tmp] = step + 1
        
        