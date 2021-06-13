class MKAverage:

    def __init__(self, m: int, k: int):
        self.m, self.k, self.data = m, k, deque() # m = 3, k = 1
        self.val = FenwickTree(10**5+1) 
        self.idx = FenwickTree(10**5+1) 

    def addElement(self, num: int) -> None:
        self.data.append(num)
        self.val.update(num, num)
        self.idx.update(num, 1)
        if len(self.data) > self.m:
            num = self.data.popleft()
            self.val.update(num, -num)
            self.idx.update(num, -1)
    
    def _bs(self, k):
        # logm  to find the left and right bound
        # 0 --- l --- r --- n
        #  (k) (m - 2k) (k)
        l, r = 0, 10**5+1
        while l < r:
            mid = (l + r) // 2
            if self.idx.query(mid) < k:
                l = mid + 1
            else:
                r = mid
        return l

    def calculateMKAverage(self) -> int:
        if len(self.data) < self.m:
            return -1
        l, r = self._bs(self.k), self._bs(self.m - self.k)
        res = self.val.query(r) - self.val.query(l)
        res += (self.idx.query(l) - self.k) * l # ？
        res -= (self.idx.query(r) - self.m + self.k) * r
        return res // (self.m - 2 * self.k)

class FenwickTree:
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, delta):
        # go down, add
        while i < len(self.sums):
            self.sums[i] += delta
            i += self._lowbit(i)

    def query(self, i):
        # go up/go to parent, sum
        s = 0
        while i > 0:
            s += self.sums[i]
            i -= self._lowbit(i)
        return s

    def _lowbit(self, x):
        # return x & (~x + 1)
        return x & -x  
    
# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()




############################
# https://leetcode.com/problems/finding-mk-average/discuss/1157928/Binary-Indexed-Trees-(BIT-or-Fenwick-tree)-%2B-Binary-lifting-(logN-Time-Complexity)


import math
from collections import deque


class BinaryIndexTree:
    def __init__(self, n: int):
        self.leng = n + 1
        """
        i is the number, nodes[i] = sum(nums[i - i & (-i), i - 1]), 
        nums is the original array
        e.g.: https://pic.leetcode-cn.com/755dd21358e8cd6ac39c85bdbaa67188dcf67dad7bd8c32d4ad777c1f376ff08-binaryindexedtreeexpandedtreewithinfo.gif
        """
        self.nodes = [0] * self.leng

    def query(self, i: int) -> int:
        """
        i is a number
        return the sum of numbers that is less than or equal to,
        which is equivalent to the sum of logN ranges (等于i代表的logi个区间的总和。)
        """
        ans = 0
        while i:
            ans += self.nodes[i]
            i -= i & -i  # remove the lowbit of i
        return ans

    def update(self, i: int, delta: int) -> None:
        while i < self.leng:
            self.nodes[i] += delta
            # parent(i) = i + i&(-i), i&(-i) is the lowbit of i,
            # e.g. i = 10, 10 = (1100)2, lowbit(1100_2) = 100_2
            i += i & -i


class MKAverage:

    def __init__(self, m: int, k: int):
        """
        Constraints:
            3 <= m <= 105
            1 <= k*2 < m
            1 <= num <= 105
            At most 105 calls will be made to addElement and calculateMKAverage.
        """
        self.max_num = 10 ** 5
        self.m = m
        self.k = k
        # self.queue_len_limit = m - 2 * k
        self.queue = deque([])
        self.queue_size = 0
        """
        self.value_tree.query(num) = the sum of the number which <= num
        self.count_tree.query(num) = the count of the number which <=num
        """
        self.value_tree = BinaryIndexTree(self.max_num)
        self.count_tree = BinaryIndexTree(self.max_num)

        self.remaining_cnt = m - 2 * k
        self.MKAverage = None  # avoid repetitive computing for MKAverage

    def addElement(self, num: int) -> None:
        self.value_tree.update(num, num)
        self.count_tree.update(num, 1)
        self.queue.append(num)
        self.queue_size += 1
        if len(self.queue) > self.m:
            removed_num = self.queue.popleft()
            self.queue_size -= 1
            self.value_tree.update(removed_num, -removed_num)
            self.count_tree.update(removed_num, -1)

        self.MKAverage = None  # avoid recomputing MKAverage if no new number added

    def search_low_boundary(self, count: int) -> int:
        """
        search the minimum num that makes self.count_tree.query(num) >= count
        即self.queue中小于等于num的数至少有count个
        e.g, input 1,
        self.value_tree.nodes = [0, 1, 3, 3, 10, 5, 11, 7, 36]
        self.count_tree.nodes = [0, 1, 2, 1, 4, 1, 2, 1, 8]
        self.max_num = 8
        i, low_boundary_num, prefix_sum
        3,   0,     0
        2,   0,     0
        1,   2,     2
        0,   2,     2

        low_boundary_num = 2, low_boundary_num + 1 = 3,
        so search_low_boundary(3) = 3 means the minimum num that makes self.count_tree.query(num) >= 3
        """
        # there are prefix_sum numbers that are less than count
        low_boundary_num, prefix_sum = 0, 0
        # self.max_num + 1 是self.count_tree.sums的长度
        for i in range(int(math.log2(self.max_num + 1)), -1, -1):
            low_boundary_num2 = low_boundary_num + (1 << i)
            # print(i, low_boundary_num, prefix_sum, low_boundary_num2)

            if low_boundary_num2 <= self.max_num and prefix_sum + self.count_tree.nodes[low_boundary_num2] < count:
                prefix_sum += self.count_tree.nodes[low_boundary_num2]
                low_boundary_num = low_boundary_num2

        # +1 because 'low_boundary_num' will have position of largest value less than 'count'
        return low_boundary_num + 1

    def calculateMKAverage(self) -> int:
        if self.queue_size < self.m:
            return -1
        if self.MKAverage is not None:
            return self.MKAverage
        low_num, high_num = self.search_low_boundary(self.k), self.search_low_boundary(self.m - self.k)
        num_sum = self.value_tree.query(high_num) - self.value_tree.query(low_num)
        """
        https://leetcode.com/problems/finding-mk-average/discuss/1152438/Python3-Fenwick-tree/903394
        Because probably there are more than k number that is less than or equal to low_num, 
        and there are more than m-k number that is less than or equal to high_num, we have to make some adjustments.
        即有的数多减了, 有的数少减了。需要重新调整
        e.g. m = 6, k = 2, nums = [1,2,2,3,3,4]
        prefix_sum = [0,1,3,5,6] prefix_sum[i] 表示 <= i的数的个数
        k1 = k, k2 = m - k = 4
        -> prefix_sum[lo=2]=3>=k1=2
        -> prefix_sum[hi=3]=5>=k2=4
        -> values_tree.query(hi)-values_tree.query(lo) = sum([1,2,2,3,3]) - sum([1,2,2]) = sum([3,3])
        But the actual solution here is sum([2,3]), we need to remove a 3 and add back a 2.
        """
        num_sum += (self.count_tree.query(low_num) - self.k) * low_num
        num_sum -= (self.count_tree.query(high_num) - (self.m - self.k)) * high_num

        # rounded down to the nearest integer
        self.MKAverage = num_sum // self.remaining_cnt
        return self.MKAverage


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()