class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Union find
        # email -> name
        # email -> index
        # index union index
        # combine all the email with the same index
        # add name for every group
        ans = []
        email2name = {}
        email2index = {}
        i = 0
        uf = DSU(10001)
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email2index:
                    email2name[email] = name
                    email2index[email] = i
                    i += 1
                uf.union(email2index[account[1]], email2index[email])
        # print(uf.parents[:len(email2index)])
        # print(email2index)
        emailGroup = collections.defaultdict(list)
        for email in email2index:
            emailGroup[uf.find(email2index[email])].append(email)
        # print(emailGroup)
        
        return [[email2name[emails[0]]] + sorted(emails) for emails in emailGroup.values()]
    
    
class DSU(object):
    def __init__(self, n):
        self.parents = [0] * n
        for i in range(n):
            self.parents[i] = i
    
    def find(self, x):
        if self.parents[x] != x: # if x is not root
            self.parents[x] = self.find(self.parents[x]) # recursion
        return self.parents[x]
    
    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)