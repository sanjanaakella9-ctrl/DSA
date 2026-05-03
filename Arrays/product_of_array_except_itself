class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
     answer = [0] * len(nums)
     zeroes = nums.count(0)
     prod = 1

     for i in range(len(nums)): 
        if  nums[i]!= 0:
         prod *= nums[i]
     
     if zeroes == 1:
        answer[nums.index(0)] = prod  
     elif zeroes == 0:
        for i in range(len(nums)):
           answer[i] = prod // nums[i]

     return answer
