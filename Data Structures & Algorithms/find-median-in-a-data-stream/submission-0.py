class MedianFinder:
    # large (minHeap), small (maxHeap)
    # heaps should be same length
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.small, num)
        
        # every # in small < # in large

        if (self.small and self.large and self.small[0] > self.large[0]):
            val = heapq.heappop_max(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop_max(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush_max(self.small, val)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(self.small[0])
        if len(self.large) > len(self.small):
            return float(self.large[0])
        
        return (float(self.small[0])+float(self.large[0]))/2
