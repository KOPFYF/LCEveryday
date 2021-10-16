class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # sort, O(nlogn) / O(n)
        # heap, O(nlogk) / O(n)
        # quick select, O(n) / O(n)
        freqs = Counter(words)
        mapping = defaultdict(list)
        for word, cnt in freqs.items():
            mapping[cnt].append(word)
        nums = list(freqs.values())
        # print(nums, mapping)
        
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
            
        freq_k = quick_select(nums, 0, len(nums) - 1, len(nums) - k)
        # print(freq_k)
        
        res = []
        for freq in sorted(mapping.keys(), reverse=True):
            words = sorted(mapping[freq])
            if freq >= freq_k:
                res += words
        return res[:k]



class Solution_heap:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = Counter(words)
        max_len = max(len(x) for x in freqs.keys())
        def encoder(word):
            # O(w)/O(w)
            out = []
            for c in list(word + ' ' * (max_len - len(word)) ):
                out.append(-ord(c))
            return tuple(out)
            
        hq = []
        for word, cnt in freqs.items(): # O(nlogk)
            heapq.heappush(hq, (cnt, encoder(word), word))
            while len(hq) > k:
                heapq.heappop(hq)
        
        res = []
        for _ in range(k):
            _, _, word = heapq.heappop(hq)
            res.append(word)
        return res[::-1]