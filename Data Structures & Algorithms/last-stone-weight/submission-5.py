class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            val1 = heapq.heappop_max(stones)
            val2 = heapq.heappop_max(stones)

            if val1 > val2:
                res = val1-val2
                heapq.heappush_max(stones, res)
        
        if len(stones) == 1:
                return stones[0]
        if len(stones) == 0:
                return 0
                


