class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        result = 0
        for i in range(len(nums)):
            if nums[i] in seen:
                result = nums[i]
            seen.add(nums[i])
        return result
        