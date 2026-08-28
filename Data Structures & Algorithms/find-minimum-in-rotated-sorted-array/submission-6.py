class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        #4,5,6,7,0,1,2
        #        l m r
        res = nums[0]
        while l<=r:
            m = (l+r)//2 # 3
            res = min(res, nums[m])
            if nums[m] >= nums[l]: 
                res = min(res, nums[l])
                l = m+1
            else:
                r = m-1
        return res

