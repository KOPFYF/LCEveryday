class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # return k smallest distances
        dists = [x**2 + y**2 for x, y in points]
        # mapping = dict(zip(dists, points)) # wrong, dist could be the same
        mapping = defaultdict(list)
        for dist, point in zip(dists, points):
            mapping[dist].append(point)
        
        def partition(nums, l, r, p):
            pivot = nums[p]
            nums[p], nums[r] = nums[r], nums[p]
            i = l
            for j in range(l, r):
                if nums[j] < pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
            nums[r], nums[i] = nums[i], nums[r]
            return i
        
        def quick_select(nums, l, r, k_smallest):
            if l == r:
                return nums[l]
            p_init = random.randint(l, r)
            p_idx = partition(nums, l, r, p_init)
            if p_idx == k_smallest:
                return nums[k_smallest]
            elif p_idx > k_smallest:
                # l --(k)-- p ---- r
                return quick_select(nums, l, p_idx-1, k_smallest)
            else:
                return quick_select(nums, p_idx+1, r, k_smallest)
            
        dist_k = quick_select(dists, 0, len(dists) - 1, k - 1)
        # print(dist_k)
        res = []
        for dist, points in mapping.items():
            if dist <= dist_k:
                res += points
        return res