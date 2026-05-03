class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            result = False
            return False 
            
        real = x
        x_ = 0
    
        while x != 0:
            digit = x % 10
            x_ = x_ * 10 + digit 
            x = x // 10
        if x_ == real:
            result = True 
            return True 
        else: 
            result = False
            return False
