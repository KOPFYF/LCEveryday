class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # time O(n) space O(n)
        d = defaultdict(int)
        mx = arr[0]
        for i in range(1, len(arr)):
            # mx is current max, if it beats current num, +1, else mx will be a bigger num
            mx = max(mx, arr[i])
            d[mx] = d[mx] + 1 
            if d[mx] >= k:
                break
        return mx
    
        # time O(n) space O(n)
        mx = arr[0]
        win = 0
        for i in range(1, len(arr)):
            if arr[i] > mx:
                # win counter, dont need dict because win has to be consecutive
                mx = arr[i]
                win = 0 
            win += 1
            if (win == k): 
                break
        return mx