class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def check(x, y):
            if y <= x * 0.5 + 7:
                return False
            elif y > x:
                return False
            elif y > 100 and x < 100:
                return False
            return True
        
        # Hash table to count
        # For each age a and each age b != a, if request(a, b), we will make count[a] * count[b] requests.
        # For each age a, if request(a, a), we will make count[a] * (count[a] - 1) requests.
        cnt = Counter(ages)
        # print(cnt)
        res = 0
        for x in cnt:
            for y in cnt:
                if check(x, y):
                    res += cnt[x] * (cnt[y] - int(x == y))
        return res
        
        
        # TLE
        n = len(ages)
        res = 0
        for x in range(n):
            for y in range(n):
                if x == y:
                    continue
                if check(x, y):
                    res += 1
        return res