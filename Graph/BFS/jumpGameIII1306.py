class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        # BFS
        dq = deque([start])
        seen = {start}
        
        while dq:
            cur = dq.popleft()
            if arr[cur] == 0:
                return True
            for i in (cur - arr[cur], cur + arr[cur]):
                if 0 <= i < len(arr) and i not in seen:
                    dq.append(i)
                    seen.add(i)
        return False


class Solution2(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        # DFS
        if start < 0 or start >= len(arr) or arr[start] < 0:
            # if index overflows or the node is visited(cycle)
            return False
        if arr[start] == 0:
            return True
        arr[start] = -arr[start] # flip visited as negative number
        
        return self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])