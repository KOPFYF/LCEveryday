class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        seen, bfs = {id}, {id}
        for _ in range(level):
            # get next level, that is, i's friends
            bfs = {j for i in bfs for j in friends[i] if j not in seen}
            # add current level to seen
            seen |= bfs
        # loop through final level and count
        freq = Counter(v for i in bfs for v in watchedVideos[i]) 
        return sorted(freq.keys(), key=lambda x:(freq[x],x))
            

class Solution2(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
            
        bfs, step, seen = deque([id]), 0, set([id])
                            
        while bfs:
            nxt_bfs = deque([])
            if step == level: break
            n = len(bfs)
            for _ in range(n):
                node = bfs.popleft()
                for nxt in friends[node]:
                    if nxt not in seen:
                        nxt_bfs.append(nxt)
                        seen.add(nxt)
            step += 1
            bfs = nxt_bfs
            
        freq = Counter(v for i in bfs for v in watchedVideos[i])  
        return sorted(freq.keys(), key=lambda x:(freq[x], x))


class Solution3:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        bfs, step, seen = deque([(id, 0)]), 0, set([id])
        ppl = []                    
        while bfs:
            node, step = bfs.popleft()
            if step == level: 
                ppl.append(node)
                continue # faster
            for nxt in friends[node]:
                if nxt not in seen:
                    bfs.append((nxt, step + 1))
                    seen.add(nxt)
            
        freq = Counter(v for i in ppl for v in watchedVideos[i])  
        return sorted(freq.keys(), key=lambda x:(freq[x], x))