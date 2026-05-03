class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            print("false")
            return False 
        flag = True
        for ch in s:
            if s.count(ch) != t.count(ch):
             flag = False 
             break 
             
        return flag 
