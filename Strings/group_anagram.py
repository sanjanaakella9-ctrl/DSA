class Solution:

    def isAnagram(self, s1: str, s2:str) -> bool:
        if len(s1) != len(s2):
            return False 

        flag = True
        for ch in s1:
            if s1.count(ch) != s2.count(ch):
             flag = False 
             break 
             
        return flag
            
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0 or len(strs) == 1:
            return [strs]
            return True 

        answer = []

        left = 0
        group = []
        used = [False]*len(strs)

        while left < len(strs):
            if used[left]:        
                left += 1
                continue
            group = [strs[left]]
            used[left] = True
            right = left + 1
            while right < len(strs):
                result = self.isAnagram(strs[left], strs[right])
                if result == True:
                    group.append(strs[right])
                    used[right] = True
                right += 1
            answer.append(group)
            left += 1

        return answer
