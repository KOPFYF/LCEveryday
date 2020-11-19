class Solution2:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # BFS + Bitmask
        # f: hash skills into id
        f = {x:1 << i for i, x in enumerate(req_skills)}
        n = len(req_skills)
        fullSkill = (1 << n) - 1
        q = [(0, [])] # start from state 00000 with no people
        ## Changed set
        cache = set()
        # level by level BFS
        while q:
            temp_q = [] # next people list
            for x, path in q: # current state, current path
                for i in range(len(people)):
                    # loop each person
                    tempx = x
                    # for person i, update state as far as possible to tempx
                    for skill in people[i]:
                        tempx |= f[skill]
                    # check end condition and return early
                    if tempx == fullSkill:
                        return path + [i]
                    if tempx not in cache:
                        cache.add(tempx) # add state
                        # since it's level-BFS, current people list must be shorter than adding more people later
                        temp_q.append((tempx, path + [i])) 
            q = temp_q



class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        # Bottom up DP, Time O(m * (2^N))
        # 1 <= req_skills.length <= 16, possible states 2^16 = 65536
        # bitmask dp with len = 1 << n, and return dp[(1 << n) - 1]
        # 1 <= people.length(m) <= 60
        
        n, m = len(req_skills), len(people)
        d = {}
        for i in range(n):
            d[req_skills[i]] = i # key is the skill, value is the id for that skill 0~(n-1)
        dp = [list(range(m)) for _ in range(1 << n)] # len(dp) = 2^n, each dp list len = m
        dp[0] = []
        # m = 3, n = 3, dp init to [[], [0, 1, 2], [0, 1, 2] ... [0, 1, 2]]
        
        # loop all people
        for i in range(m):
            # find the skills for current guy i
            skill = 0
            # loop each skill for this guy
            for s in people[i]:
                skill |= (1 << d[s]) # bitmask all skills for this guy
            # try to add this guy to all possible states
            for k, v in enumerate(dp): 
                # k is the current state(0 to 2^n-1), v is the current list of people
                # add current guy's all skillsets to each dp state and update skill
                # for example, n = 5, k = 00111, skill = 01000, newskill = 01111
                # v = [0, 1, 3], dp[newskill] = dp[01111] = [0, 1, 2, 3, 4](init list)
                # i = 2, after adding i, v + [i] = [0, 1, 2, 3] < [0, 1, 2, 3, 4]
                new_skill = k | skill
                if new_skill != k and len(dp[new_skill]) > len(v) + 1:
                    # new_skill != k: we got marginal benefit, more skills satisfied
                    # len(dp[new_skills]) > len(v) + 1: new skill requires less people
                    dp[new_skill] = v + [i] # update people list
        return dp[(1 << n) - 1]
                
            


class Solution3:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # Top down DP
        res = [''] * 17
        n = len(req_skills)
        def dfs(idx, has, path):
            # idx: current skill we request
            # has: current total skillset
            # path: current path
            nonlocal res
            if idx == n:
                # to the end
                res = path
            elif req_skills[idx] in has:
                # we already cover this skill in our skillset
                dfs(idx + 1, has, path)
            else:
                if len(path) + 1 < len(res):
                    # only when current people list + 1 shorter than current optimal list
                    for i, p in enumerate(people):
                        p = set(p) # set of current person's skillset
                        if req_skills[idx] in p:
                            # if current person has the cur skill we need, add him
                            union = p & has # pruning redudant skills for current person
                            has |= p # update skillsets
                            # recursion
                            dfs(idx + 1, has, path + [i])
                            # remember to recover 'has' set
                            has -= p # remove impact from current guy
                            has |= union # recover what we prune before
        dfs(0, set(), [])
        return res