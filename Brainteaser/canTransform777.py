class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end): return False
        
        A = [(s, i) for i, s in enumerate(start) if s in ('L', 'R')]
        B = [(e, i) for i, e in enumerate(end) if e in ('L', 'R')]
        
        if len(A) != len(B): return False
        
        for (s, i), (e, j) in zip(A, B):
            if s != e:
                return False
            if s == 'L' and i < j:
                return False
            if s == 'R' and i > j:
                return False
            
        return True