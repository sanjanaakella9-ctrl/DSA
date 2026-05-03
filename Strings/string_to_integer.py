class Solution:
    def myAtoi(self, s: str) -> int:

        #whitespaces
        result = ""
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        result = s[i:]
        
        if result == "":
         return 0

        #sign 
        if result[0] == "-":
            sign = 0
            result = result[1:]
        elif result[0] == "+": 
            sign = 1
            result = result[1:]
        else: sign = 1 

        #leading zeroes
        count = 0
        for j in range(0, len(result)):
            if result[j] == '0':
                count += 1
            else: 
                break
        result = result[count:]
        
        #final
        answer = ""
        for k in range(0, len(result)):
            if result[k] >= '0' and result[k] <= '9':
                answer += result[k]
            else: 
                break 

        if sign == 0:
            answer = "-" + answer 

        
        
        if answer == "" or answer == "-":
          return 0
          return False 

        
        num = int(answer)
        if num > 2**31 - 1:
           num = 2**31 - 1
        elif num < -2**31:
            num = -2**31

        return num
