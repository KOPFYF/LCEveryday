import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # quick sort, O(n)
        freqs = Counter(nums)
        arr = [(f, num) for num, f in freqs.items()]
        
        def partition(arr, l, r, p):
            pivot = arr[p]
            arr[p], arr[r] = arr[r], arr[p]
            
            i = l
            for j in range(l, r):
                if arr[j][0] < pivot[0]:
                    arr[j], arr[i] = arr[i], arr[j]
                    i += 1
            
            arr[r], arr[i] = arr[i], arr[r]
            return i
        
        def quick_select(arr, l, r, k_smallest):
            if l >= r:
                return
            p_rand = random.randint(l, r)
            p = partition(arr, l, r, p_rand)
            if p == k_smallest:
                return
            elif p < k_smallest:
                quick_select(arr, p+1, r, k_smallest)
            else:
                quick_select(arr, l, p-1, k_smallest)
        
        quick_select(arr, 0, len(arr)-1, len(arr)-k-1)
        return [num for f, num in arr[-k:]]



class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort, O(n)
        buckets = [[] for _ in range(len(nums) + 1)]
        number_count = collections.defaultdict(int)
        for num in nums:
            number_count[num] += 1
            
        for num, freq in number_count.items():
            buckets[freq].append(num)
        
        # buckets is a double array
        flat_list = []
        # traverse from right to left so number with higher frequency come first
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            if bucket:
                for num in bucket:
                    flat_list.append(num) # call you out!!
        return flat_list[:k]


import heapq
from collections import Counter
class Solution2:
    # heap O(nlogn) -> O(nlogk)
    def topKFrequent(self, nums, k):
        res = []
        dic = Counter(nums)
        max_heap = [(-val, key) for key, val in dic.items()]
        heapq.heapify(max_heap)
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res  



class Solution2(object):
    # no need extra dic
    def topKFrequent(self, nums0, k0):
        counts = collections.Counter(nums0) # {1:3, 2:2, 3:1}
        freq = list(counts.values()) # [3,2,1] k = 2 => 3, 2 (map)=> [1, 2]
        freq2num = defaultdict(list)
        for k, v in counts.items():
            freq2num[v].append(k) # diff num could have same freq
            
        def partition(freq, l, r, p):
            # pick pivot and move it to the right
            pivot = freq[p]
            freq[p], freq[r] = freq[r], freq[p]
            
            # move smaller item to the left
            i = l
            for j in range(l, r):
                if freq[j] < pivot:
                    freq[j], freq[i] = freq[i], freq[j]
                    i += 1 # now i is the pivot index
            
            # move pivot to the correct place
            freq[r], freq[i] = freq[i], freq[r]
            return i # return the pivot index
            
        def quick_select(freq, l, r, k_smallest):
            if l == r:
                return freq[l]
            p = random.randint(l, r)
            p_idx = partition(freq, l, r, p)
            if p_idx == k_smallest:
                return freq[p_idx]
            elif p_idx > k_smallest:
                # l, ---- k ----(p)---r
                return quick_select(freq, l, p_idx-1, k_smallest)
            else:
                return quick_select(freq, p_idx+1, r, k_smallest)
        
        pick_freq = quick_select(freq, 0, len(freq)-1, len(freq)-k0)
        # print(pick_freq, freq2num[pick_freq])
        res = []
        for freq, num in freq2num.items():
            if freq >= pick_freq:
                res += num
        return res
        
        