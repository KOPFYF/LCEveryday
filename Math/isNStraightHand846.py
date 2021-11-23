class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        # O(wlogw + mw)
        n = len(hand)
        if n % groupSize != 0:
            return False
        cnt = Counter(hand)
        for num in sorted(cnt):
            if cnt[num] > 0:
                tmp = cnt[num]
                for diff in range(groupSize):
                    # if you do it in the normal order, c[i] will become 0 first,
                    # print(num, diff, cnt)
                    cnt[num + diff] -= tmp
                    if cnt[num + diff] < 0:
                        return False
        return True