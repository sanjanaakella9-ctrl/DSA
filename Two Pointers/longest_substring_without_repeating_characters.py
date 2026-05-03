class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        l_max = 0
        l = 0

        answer = set()

        for right in range(len(s)):
            while s[right] in answer:
                answer.remove(s[left])
                left += 1
                l -= 1
            
            answer.add(s[right])
            right += 1 
            l += 1
            if l > l_max:
                l_max = l 
        return l_max
