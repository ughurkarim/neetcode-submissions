class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)   # userId -> list of [time, tweetId]
        self.followMap = defaultdict(set)    # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        # Ensure the user always follows themselves to see their own tweets
        self.followMap[userId].add(userId)

        # 1. Populate the max-heap with the most recent tweet from each followee
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                # Negate time to simulate a max-heap in Python's min-heap
                maxHeap.append([-time, tweetId, followeeId, index - 1])

        # 2. Heapify the list (O(N) time where N is number of followees)
        heapq.heapify(maxHeap)

        # 3. Extract the 10 most recent tweets
        while maxHeap and len(res) < 10:
            neg_time, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)

            # If the followee has older tweets, push the next one into the heap
            if index >= 0:
                time, nextTweetId = self.tweetMap[followeeId][index]
                heapq.heappush(maxHeap, [-time, nextTweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Ensure a user cannot unfollow themselves
        if followeeId in self.followMap[followerId] and followeeId != followerId:
            self.followMap[followerId].remove(followeeId)