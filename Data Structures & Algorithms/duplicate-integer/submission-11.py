class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for number in nums:
            if number not in seen:
                seen.add(number)
            else:
                return True
        return False