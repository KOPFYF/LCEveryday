# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    follow up: What if the linked list is extremely large and its length is unknown to you
    Reservoir Sampling, randomly choosing k samples from a list of n items, where n is either a very large or unknown number
    It works for streaming/dynamic data with O(n) time
    prob of each item being selected/kept = k/n
    prob of being kept = k/(k+1) * (k+1)/(k+2) * ... * (n-1)/n = k/n
    here k = 1, n = inf
    
    Algorithm:
    1) Create an array reservoir[0..k-1] and copy first k items of stream[] to it. 
    2) Now one by one consider all items from (k+1)th item to nth item. 
        2a) Generate a random number from 0 to i where i is the index of the current item in stream[]. Let the generated random number is j. 
        2b) If j is in range 0 to k-1, replace reservoir[j] with stream[i]
    '''
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
            
            
    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        res = self.head.val
        cur = self.head.next
        idx = 1
        
        while cur:
            if random.randint(0, idx) == 0:
                # for idx-th number, keep it with a prob 1/idx
                res = cur.val # substitute the sampling
            cur = cur.next
            idx += 1
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()