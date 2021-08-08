class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # LIS, O(nlogn)/O(n)
        lis, res = [], [] # lis is a mono inc list

        for h in obstacles:
            if not lis or h >= lis[-1]:
                # h in the end of LIS
                lis.append(h)
                res.append(len(lis))
            else:
                # h in the middle of LIS
                # bisect right because it's non-decreasing
                # if strictly increasing, we should use bisect left
                idx = bisect.bisect_right(lis, h)
                lis[idx] = h # replace that number with h
                res.append(idx + 1)

            # print(lis, res)

        return res