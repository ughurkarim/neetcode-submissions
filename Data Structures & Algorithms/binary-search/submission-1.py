class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r) // 2 #3+5//2 = 4
            if nums[m] < target: #nums[2] = 2 < 4
                l = m+1 #l = 3
            elif nums[m] > target:
                r = m-1
            elif nums[m] == target:
                return m
        return -1