# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    # https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/discuss/193873/Most-elegant-and-simple-solution-in-Python
    def __init__(self):
        self.dq = deque()
        
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while i < n:
            if self.dq:
                buf[i] = self.dq.popleft()
                i += 1
            else:
                buf4 = [' '] * 4
                cnt = read4(buf4)
                if cnt == 0:
                    break
                self.dq += buf4[:cnt]
        return i

