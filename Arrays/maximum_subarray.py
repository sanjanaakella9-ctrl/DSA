class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0] 
        sum2 = 0
        if len(nums) == 1:
            sum = nums[0] 
        else: 
            for i in range(len(nums)):
                if nums[i] < sum2 + nums[i]:
                    sum2 += nums[i]
                else: 
                    sum2 = nums[i]
                if sum2 > sum:
                        sum = sum2 
                elif sum2 < 0:
                        sum2 = 0
         
        return sum
