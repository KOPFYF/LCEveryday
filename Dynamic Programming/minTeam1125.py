class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
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
                
            
        