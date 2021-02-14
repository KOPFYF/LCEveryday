class FreqStack:
    # stack, only care max_freq
    def __init__(self):
        self.freq = collections.Counter() # count the frequence of elements.
        self.m = collections.defaultdict(list) # a map of stack
        self.maxf = 0 # maxfreq records the maximum frequence

    def push(self, x):
        # freq, m = self.freq, self.m
        self.freq[x] += 1
        self.maxf = max(self.maxf, self.freq[x])
        self.m[self.freq[x]].append(x)

    def pop(self):
        # freq, m, maxf = self.freq, self.m, self.maxf
        x = self.m[self.maxf].pop()
        if not self.m[self.maxf]: 
            self.maxf = self.maxf - 1
        self.freq[x] -= 1
        return x
    