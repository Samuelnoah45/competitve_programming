class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        l = 0
        r = len(nums) -1 
        ans = 0
        while l < r:
            
            sums = nums[l] + nums[r]
            
            if sums == k :
                ans += 1
                r -= 1
                l += 1
            elif sums < k:
                l += 1
            else:
                r  -= 1
        return ans