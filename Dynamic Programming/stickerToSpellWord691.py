class Solution2:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # DFS + memo
        cnt = Counter(target) # dict of freq we need to deal with
        res, n = float('inf'), len(target)
        
        def dfs(d, used, pos):
            # d: dict of freq of current stickers
            # used: number of candidate stickers
            # pos: index of target we are checking
            # Nonlocal variables are used in nested functions whose local scope is not defined. 
            # This means that the variable can be neither in the local nor the global scope.
            nonlocal res # avoid UnboundLocalError
            if pos == n:
                res = used # loop to the end
            elif d[target[pos]] >= cnt[target[pos]]:
                # use the current sticker and move the pointer
                dfs(d, used, pos + 1)
            elif used + 1 < res:
                # update only when current result(res) is not optimal
                for sticker in stickers:
                    # try next sticker by looping all
                    if target[pos] in sticker:
                        for s in sticker:
                            # add all chars to the dict
                            d[s] += 1
                        dfs(d, used + 1, pos + 1)
                        for s in sticker:
                            # delete dict information after the call
                            d[s] -= 1
        
        dfs(defaultdict(int), 0, 0)
        return res if res < float("inf") else -1
        

class Solution1(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        n = len(target)
        # dp[]
        dp = collections.defaultdict(int)
        # Step 1: preprocessing the words
        # s is the dict freq we need to satisfy
        # A is to build dict for each sticker and remove non-overlapping chars
        s = collections.Counter(target)
        A = [collections.Counter(stick) & s for stick in stickers]
        # ('s:', Counter({'h': 2, 't': 2, 'a': 1, 'e': 1}))
        # ('A:', [Counter({'h': 1, 't': 1}), Counter({'a': 1, 'e': 1}), Counter({'e': 1})])
        # ["with", "example", "science"], "thehat" ==> ["th", "ea", "e"], "thehat" 
        # also pop out non-strong stickers, for example, "e" is no need cause we have "ea"
        # cost O(m^2), m is the length of stickers
        for i in range(len(A) - 1, -1, -1):
            if any(A[i] & A[j] == A[i] for j in range(len(A)) if i != j):
                A.pop(i)
        
        # Step 2: Bit Mask
        # The idea is to use # from 0 to 2^n-1 as bitmap to represent every subset of target
        # Then populate all of these subset from 0 to 2^n-1 by applying 1 sticker at each time.
        # Eventually you might or might not get the ultimate result 2^n-1, aka target.
        # "thehat": 111111, ["th", "ea"] : ["110000",001010"]
        for i in range(1 << n):
            # for every subset i, start from 00000...(emptyset) to 111111...(the target)
            if dp[i] == 0 and i != 0:
                continue
            for a in A:
                # try use each sticker as an char provider to populate a super-set of i
                nex = i
                has = a.copy()
                for pos in range(n):
                    if i & (1 << pos) != 0 or has[target[pos]] == 0:
                        # if pos is already done or we dont have such supply
                        continue
                    else:
                        # try apply it on a missing char in the subset of target
                        # and set the bit on pos to 1
                        nex |= (1 << pos)
                        has[target[pos]] -= 1
                if i != nex:
                    dp[nex] = dp[i] + 1 if dp[nex] == 0 else min(dp[nex], dp[i] + 1)
        return -1 if dp[(1 << n) - 1] == 0 else dp[(1 << n) - 1]






