class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        str = ''
        for ch in s:
            if (('a' <= ch <= 'z') or ('0' <= ch <= '9')):
                str += ch
        
        left = 0
        right = len(str) - 1

        while left < right:
            if str[left] == str[right]:
                left += 1
                right -= 1
            else: 
                return False 

        return True
