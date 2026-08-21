class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        maxCount = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            
            if nums[i] != nums[i-1]+1:
                count = 1
            else: 
                count += 1
                maxCount = max(maxCount, count)

        return maxCount

        
