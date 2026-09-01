class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        result = 0
        i = 1
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                result = nums[i]

        return result

        