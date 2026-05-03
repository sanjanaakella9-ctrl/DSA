class Solution:
    def intToRoman(self, num: int) -> str:
        
        roman = ""

        #thousands
        m = num//1000
        num = num - m*(1000)
        roman += "M" * m

        #100
        k = num//100
        if k == 9:
            roman += "CM"
            num = num - 9 * (100)
        else:
            d = num//500 
            num = num - d*(500)
            roman += "D" * d
            c = num//100 
            num = num - c*(100)
            if c == 4:
             roman += "CD"
            else:
             roman += "C" * c

        n = num//10  
        if n == 9:
            roman += "XC"
            num = num - 9 * (10)
        else:
            #50
            l = num//50 
            num = num - l*(50)
            roman += "L" * l

            #10
            x = num//10 
            num = num - x*(10) 
            if x == 4:
                roman += "XL"
            else: 
                roman += "X" * x

        #last
        v = num//5 
        num = num - v*(5)
        num1 = num
        i = num//1 
        if v == 0:
            if num1 == 4:
                roman += "IV"
            else: 
                roman += "I" * i
        else:
            if num1 == 4:
                roman += "IX"
            else: 
                roman += "V" + "I" * i 

        return roman 
