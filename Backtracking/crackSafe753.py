class Solution0(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Starting from all 0's, then dfs traverse each possibility and backtrack if not possible.
        def dfs(curr, counted, total):
            if len(counted)==total:
                return curr
            
            for i in range(k):
                tmp = curr[-(n-1):]+str(i) if n!=1 else str(i)
                if tmp not in counted:
                    counted.add(tmp)
                    res = dfs(curr+str(i), counted, total)
                    if res:
                        return res
                    counted.remove(tmp)
                    
        return dfs("0"*n, set(["0"*n]), k**n)


class Solution1(object):        
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = "0" * (n - 1)
        visits = set()
        for x in range(k ** n):
            current = ans[-n+1:] if n > 1 else ''
            for y in range(k - 1, -1, -1):
                if current + str(y) not in visits:
                    visits.add(current + str(y))
                    ans += str(y)
                    break
        return ans


from itertools import product

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        """
        The strategy to crack the safe is to try all the code combinations. As 
        the safe is designed in the way that it always reads the last `n` digits 
        keyed in, there are opportunities that we can reuse the common digits 
        shared between contiguous combinations and thus save certain key 
        strokes. Herein, the problem asks for one working code sequence that has 
        the minimum length and thus saves us the most key strokes. 

        Obviously, given a safe with a k-digit pad and n-digit password length, 
        to crack it with brute force, there are `k^n` combinations to try, so 
        the worst case is that we key in every single combination and get a 
        sequence with a length of `n * k^n`. But there are definitely certain 
        common digits shared among the combinations, which we can leverage to 
        shorten the sequence. The crux is the order to try all the combinations 
        that exploits the common ground. 

        If we think of every combination as a node in the graph, the common 
        ground between the combinations is the edge between every pair of nodes, 
        which allows a combination to be transformed to another by removing the 
        first digit at the front and adding a new digit to the end. Our goal is 
        to go over all the nodes in a single pass, since we don't want to try a
        combination twice to prolong the code sequence. Intuitively, we try to 
        find an euler path from such graph. A known algorithm to find an euler 
        path is Hierholzer's, which has been thoroughly introduced here: 
        https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/ 
      
        """
        # generate all the possible combinations with the given `n` and `k`, 
        # which are the nodes in the graph and the edges are implicitly created 
        # if any pair of combinations have certain digit sequence in common
        perms = set(map(lambda x: ''.join(x), product(map(str, range(k)), repeat=n)))
        # print(perms)
        res = []
        
        # run DFS to traverse all the nodes in the graph and remove them once 
        # they being visited. Removing a node also implicitly removes the 
        # edge(s) to the combinations it can be transformed to
        def dfs(n):
            # stop when the graph is empty
            if not perms:
                return
            for d in map(str, range(k)):
                # transform the current combination to another by removing the 
                # digit at the front and appending a digit to the end
                next_ = (n + d)[1:]
                # check if the new combination is still reachable, i.e. if it is 
                # not yet visited and the edge to it still exists
                if next_ in perms:
                    # if it is not yet visited, remove it from the graph and 
                    # visit it next
                    perms.remove(next_)
                    dfs(next_)
                    # according to Hierholzer's, we can only add a node to an 
                    # euler path until it has no edges to other nodes. So we 
                    # visit the node first to remove all its edges to others 
                    # first and add the node to the path then
                    res.append(d)
        
        # start with all digits set to 0
        start = '0' * n
        # remove the start from the graph
        perms.remove(start)
        
        # start the traversal
        dfs(start)
        
        # add the start to the end of the path to form the euler circuit
        return ''.join(res) + start