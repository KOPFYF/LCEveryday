class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = defaultdict(list)
        self.follower = defaultdict(set) # key follows val
        self.order = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId] += [(self.order, tweetId)]
        self.order -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        # heap = self.tweets[userId]
        # heapq.heapify(heap)
        # while len(heap) > 10:
        #     heapq.heappop(heap)
        # # print(heap)
        # for user in self.follower[userId]:
        #     for order, tid in self.tweets[user]:
        #         heapq.heappush(heap, (order, tid))
        #         while len(heap) > 10:
        #             heapq.heappop(heap)
        # return [news for _, news in heap]
                
        tweets = sorted(tw_id for user in self.follower[userId] | {userId} for tw_id in self.tweets[user])[:10]
        return [news for i, news in tweets]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follower[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follower[followerId].discard(followeeId)
#         remove(elem): Remove element elem from the set. Raises KeyError if elem is not contained in the set.

# discard(elem): Remove element elem from the set if it is present.


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)