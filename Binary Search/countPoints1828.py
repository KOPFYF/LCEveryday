'''
O(n) hint:
we can sort points first by one of the coordinates, and only process points in [qx - r, qx + r] interval. We can use binary search to find the start of that interval.

It's not as good as VP trees, and still O(n) in the worst case, but it's better than brute force in the average case.

Instead of VP trees, we could also use KD trees. I believe that KD trees are much easier to implement.



sort + binary search

sort the points by x
for every query, check the range of points between the lower bound and the upper bound(u can also binary search the points by y, but it's a bit more complicated and it doesn't perform a lot essentially because the testcases are small)
Time O(PlogP + NlogP)
Space O(N)
1900 ms, faster than 100.00%

'''

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        points.sort(key=lambda el: (el[0], el[1]))
        n = len(queries)
        res = n * [0]
        for i in range(n):
            x, y, r = queries[i]
            left = self.lowerBsearch(points, x-r)
            right = self.upperBsearch(points, x+r)
            for j in range(left, right):
                _x, _y = points[j]
                if (_x - x)**2 + (_y - y)**2 <= r**2:
                    res[i] += 1
        return res

    def lowerBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target <= nums[mid][0]:
                right = mid
            else:
                left = mid + 1
        return left

    def upperBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target >= nums[mid][0]:
                left = mid + 1
            else:
                right = mid
        return right


class Solution_brute_force:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        # brute force
        def count(query, points):
            x0, y0, r0 = query
            res = 0
            for x, y in points:
                if (x - x0) ** 2 + (y - y0) ** 2 <= r0 ** 2:
                    res += 1
            return res
        
        return [count(query, points) for query in queries]