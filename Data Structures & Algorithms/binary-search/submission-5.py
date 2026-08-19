class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        candidate = -1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] >= target:
                candidate = m
                r = m - 1 
            else:
                l = m + 1
        
        return candidate if nums[candidate]==target else -1

