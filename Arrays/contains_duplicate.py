class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        okay = set()
        for num in nums: 
            if num in okay:
                print("true")
                return True
            okay.add(num)
        else: 
            print("false")
            return False 
            
