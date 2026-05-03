class Solution:
    def reverse(self, x: int) -> int:
        uwu = 0
        original = x
        if x < 0:
            x = -x 
        while x != 0:
            digit = x % 10
            uwu = uwu*10 + digit
            x = x // 10
        if uwu < -2**31 or uwu > 2**31 - 1:
          return 0
        else: 
            if original < 0:
                return -uwu
            else:
                return uwu
