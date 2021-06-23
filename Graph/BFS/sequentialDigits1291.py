class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # BFS
        out = []
        dq = deque(range(1,10))
        while dq:
            num = dq.popleft()
            if low <= num <= high:
                out.append(num)
            last_digit = num % 10 # if possible, extract last bit and +1
            if last_digit < 9: 
                dq.append(num * 10 + last_digit + 1)
                    
        return out