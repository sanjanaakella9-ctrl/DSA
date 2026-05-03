class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
     nums.sort()
     answer = []
     for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
        
            i = k + 1 #left pointer 
            j = len(nums) - 1 #right pointer
            while i < j: 
                sum = nums[k] + nums[i] + nums[j]
                if  sum == 0:
                 answer.append([nums[k], nums[i], nums[j]])
                 i += 1
                 j -= 1
            
                 while i < j and nums[i] == nums[i - 1]:
                        i += 1

                 while i < j and nums[j] == nums[j + 1]:
                        j -= 1

                elif sum < 0:
                    i += 1

                else: 
                    j -= 1 
     return answer
