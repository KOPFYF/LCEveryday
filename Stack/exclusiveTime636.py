class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        # stack
        res = [0] * n
        stack = [] # store hanging function id 
        # prev = 0
        
        for log in logs:
            f, se, t = log.split(':')
            f, t = int(f), int(t)
            if se == 'start':
                # if start, hang up last fid and cumulate the time
                if stack:
                    res[stack[-1]] += t - prev
                stack.append(f)
                prev = t
            else:
                # if end, wrap up current fid
                res[stack.pop()] += t - prev + 1
                prev = t + 1
        return res