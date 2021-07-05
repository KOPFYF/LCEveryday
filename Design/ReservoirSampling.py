# https://www.cnblogs.com/snowInPluto/p/5996269.html


import random

def reservoir_sampling_one(input_array):
    reservoir = [input_array[0]]
    for i in range(len(input_array)): 
        rand_idx = random.randrange(0, i + 1)
        if rand_idx == 0:
            reservoir[0] = input_array[i]
    return reservoir


def reservoir_sampling_k(input_array, k):
    """
    Returns @param k random items from @param iterable of size n.
    """
    reservoir = []
    for t, item in enumerate(input_array):
        if t < k:
            # choose with prob = 1 when pool size < k
            reservoir.append(item) 
        else:
            # starting from k+1 item, use it to substitute the first k items
            # for example, when t = k + 1, first random sampling with prob k/(k+1) to sub, 
            # then pick one of k, we have 1/(k+1) to kick it out, the remain prob would be 1-1/(k+1) = k/(k+1) for each of k items 
            # when t = k + 2, the first k items remaining prob would be 1-k/(k+2)*(1/k) = (k+1)/(k+2) 
            # then when we are in step n, the first k items remaining prob would be: k/n (like chain rule)
            m = random.randint(0, t) 
            if m < k: # if m in range [0, k-1], kick such m out
                reservoir[m] = item
    return reservoir


class RESERVOIR_SAMPLING():
    def __init__(self, k=1000):
        self.reservoir = [] # sample container of size at most k
        self.k = k # sample size
        self.i = 0

    def add_to_reservoir(self, sample):
        self.i += 1
        if(self.k >= self.i):
            self.reservoir.append(sample)
        else:
            # randint(a,b) gives a<=int<=b
            j = random.randint(0, self.i - 1)
            if j < k:
                self.reservoir[j] = sample

k = 10
samples = [i for i in range(10)] * k
res = RESERVOIR_SAMPLING(k)
for sample in samples:
    res.add_to_reservoir(sample)

print(res.reservoir)