class Twitter:

    def __init__(self):
        self.count = 0  #to store time(cnt) of tweet posted
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId
      
    def postTweet(self, userId: int, tweetId: int) -> None:
        #each user 1/more tweet
        #hashmap of userid->list of tweets ; O(1) time
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        #hashmap of userid->list of tweets ; O(1) time
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res #latest 10 tweets in feed

    def follow(self, followerId: int, followeeId: int) -> None:
        #userId->hashset of followee ; O(1) time
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #userId->hashset of followee ; O(1) time
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


    #10 most recent tweets->nd of list id's from 2nd hashMap
    #...so maintain time(cnt) of tweet to get most recent 10
    #maintained in [count,tweetId]
    #nw to see who the tweet lies to from 1st hashmap->has the userId
    