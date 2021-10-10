class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        1 <= task.length <= 104
        tasks[i] is upper-case English letter.
        The integer n is in the range [0, 100]
        
        case 1: A ... (n) ... A ... (n) ... A ... (n) ... | A B C D D EEE
        case 2: A ... (n) ... A ... (n) ... A ... (n) ... | A B 
        
        case2: f_max: freq of A, B
        (f_max - 1) * (n + 1) + n_max
        
        case1: the gap in between is not enough -> len(tasks)
        
        '''
        
        cnt = Counter(tasks)
        freqs = list(cnt.values())
        f_max = max(freqs)
        n_max = freqs.count(f_max)
        case2 = (f_max - 1) * (n + 1) + n_max
        case1 = len(tasks)
        
        return max(case1, case2)