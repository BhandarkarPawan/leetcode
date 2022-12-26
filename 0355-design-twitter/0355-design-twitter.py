from collections import defaultdict, OrderedDict

class Twitter:
    
    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.following = defaultdict(set)
        self.counter = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.counter, tweetId))
        self.counter += 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] 
        
        followingTweets = [self.tweetMap[x][-10:] for x in  self.following[userId]]
        followingTweets.append(self.tweetMap[userId][-10:])
        flattened = [x for y in followingTweets for x in y]

        return [x[1] for x in sorted(flattened, key=lambda a : -a[0])][:10]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].remove(followeeId)