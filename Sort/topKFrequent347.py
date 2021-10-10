import collections

class Solution(object):
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
        
        