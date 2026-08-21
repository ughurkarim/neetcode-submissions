class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        for n, c in count.items():
            result[c].append(n)
        
        answer = []

        for i in range(len(result)-1, 0, -1):
            for n in result[i]:
                answer.append(n)
            if len(answer) == k:
                return answer
        

        