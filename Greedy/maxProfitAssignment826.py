class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Time O(JlogJ + WlogW), Space O(JlogJ)
        # sort by easiser job first, smallest profit first
        jobs = sorted(zip(difficulty, profit)) 
        worker.sort()

        res = 0
        j = 0
        best_profit = 0

        # O(W + J)
        # Sorting ensures efficient pairing of workers with jobs 
        # based on their abilities and job difficulties.
        for w in worker:
            while j < len(worker) and w >= jobs[j][0]:
                best_profit = max(best_profit, jobs[j][1]) # get best profit for each worker
                j += 1
            res += best_profit
        
        return res


