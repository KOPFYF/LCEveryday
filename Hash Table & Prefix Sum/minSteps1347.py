class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        store = Counter(s)
        res = 0
        
        for ch in t:
            if store[ch] > 0:
                store[ch] -= 1
            else:
                res += 1
        return res


'''
https://www.1point3acres.com/bbs/thread-811698-1-1.html

Q1) 给一个restaurant名字，和一个list的相似名字。一个名字如果swap任意两个char等于given name就是相似名字eg. 
given: "omega"
similar: oemga, omeag, omega
not similar: ommga, omegaa
用4个变量存两个不一样的char和他们的index即可，等到遍历到下一组不一样的char，看index和是不是和之前存的相反就好
'''
def check(s1, s2):
    index_diff = set()
    for i, (ch1, ch2) in enumerate(zip(s1, s2)):
        # print(ch1, )
        if ch1 != ch2:
            index_diff.add(i)
    return index_diff

s = "omega"
ls = ["oemga", "omeag", "omega", "ommga", "omegaa"]

def check_lists(s, ls):
    res = []
    for cand in ls:
        if len(cand) != len(s):
            res.append([cand, False])
        else:
            diff = check(s, cand)
            if len(diff) == 2 or len(diff) == 0:
                res.append([cand, True])
            else:
                res.append([cand, False])
    return res


print(check_lists(s, ls))




















