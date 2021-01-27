'''
m = 8
1 << 8 - 1
1 0000 0000 => 1111 1111
transform from zero to full mask
'''

class Solution1:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # bit mask DP
        m, n = len(req_skills), len(people)
        mapping = {skill : i for i, skill in enumerate(req_skills)} # skill to index
        skill_masks = [0] * n # for each people they have a skill mask
        for i, p in enumerate(people):
            for skill in p:
                if skill in mapping: # skip skills not in mapping
                    skill_masks[i] |= (1 << mapping[skill]) # 0000 0001 | 0000 0010 => 0000 0011
        
        full_mask = (1 << m) - 1
        @lru_cache(None)
        def dfs(mask):
            if mask == full_mask: return []
            
            res = [0] * (n + 1) # like res = float('inf')
            for i, skill_mask in enumerate(skill_masks): # loop each person
                nxt_mask = mask | skill_mask
                if nxt_mask == mask: # skip useless/duplicated person
                    continue
                res = min(res, [i] + dfs(nxt_mask), key=len) # take person i or not take
            return res        
        return dfs(0)


class Solution2_9000ms:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # bit mask DP, 0-1 knapsack, O(n^2 2^m)
        m, n = len(req_skills), len(people)
        mapping = {skill : i for i, skill in enumerate(req_skills)} # skill to index
        skill_masks = [0] * n # for each people they have a skill mask
        for i, p in enumerate(people):
            for skill in p:
                if skill in mapping: # skip skills not in mapping
                    skill_masks[i] |= (1 << mapping[skill]) # 0000 0001 | 0000 0010 => 0000 0011
        
        full_mask = (1 << m) - 1
        @lru_cache(None)
        def dfs(i, mask):
            # O(n^2 2^m)
            if i == n: 
                return [] if mask == full_mask else [0] * (n + 1)
            
            res = dfs(i + 1, mask) # no take person i
            for j in range(i + 1, n + 1):
                nxt_mask = mask | skill_masks[i] # take person i
                res = min(res, [i] + dfs(j, nxt_mask), key=len) # take person i or not take
            return res  
        
        return dfs(0, 0)