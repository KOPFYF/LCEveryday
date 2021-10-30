# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

'''
Get data from read4 and store it in a queue
Transfer data from queue to buf

'''
class Solution:
    def __init__(self):
        self.dq = deque()
    
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while i < n:
            if self.dq:
                # popleft and add it to buf
                buf[i] = self.dq.popleft()
                i += 1
            else:
                # pre-load deque()
                buf4 = [''] * 4
                cnt = read4(buf4)
                if not cnt:
                    break
                self.dq += buf4[:cnt]
        return i