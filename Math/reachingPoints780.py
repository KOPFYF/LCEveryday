class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # reverse search, O(log(min(tx,ty)))
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx
        # print(tx, ty) # 3 % 5 = 3, 5 % 3 = 2 => 3 % 2 = 1, 2 % 3 = 2
        # now one of them is matched
        return sx == tx and sy <= ty and (ty - sy) % sx == 0 or \
               sy == ty and sx <= tx and (tx - sx) % sy == 0 