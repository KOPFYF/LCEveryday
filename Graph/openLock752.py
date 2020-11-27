class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        # BFS
        dead_set = set(deadends)
        queue = collections.deque([('0000', 0)])
        visited = set(['0000'])

        while queue:
            numstr, steps = queue.popleft()
            if numstr == target:
                return steps
            elif numstr in dead_set:
                continue # skip current loop
            for i in range(4):
                digit = int(numstr[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10 # make sure it's positive
                    new_numstr = numstr[:i] + str(new_digit) + numstr[i + 1:]
                    if new_numstr not in visited:
                        visited.add(new_numstr)
                        queue.append((new_numstr, steps + 1))
        return -1