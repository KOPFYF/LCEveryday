class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # BFS
        f = {x:1 << i for i,x in enumerate(req_skills)}
        n = len(req_skills)
        full_mask = (1 << n) - 1
        bfs, seen = [(0, [])], set() # start from state 00000 with no people
        # level by level BFS
        while bfs:
            nxt_bfs = [] # next people list
            for mask, path in bfs: # current state, current path
                for i in range(len(people)):
                    # loop each person
                    nxt_mask = mask
                    # for person i, update state as far as possible to nxt_mask
                    for skill in people[i]:
                        nxt_mask |= f[skill]
                    # check end condition and return early
                    if nxt_mask == full_mask: return path + [i]
                    
                    if nxt_mask not in seen:
                        seen.add(nxt_mask) # add state
                        # since it's level-BFS, current people list must be shorter than adding more people later
                        nxt_bfs.append((nxt_mask, path + [i])) 
            bfs = nxt_bfs