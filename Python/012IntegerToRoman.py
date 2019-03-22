# 012 Integer to Roman
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        M = ["", "M", "MM", "MMM"]
        return M[num/1000] + C[num%1000/100] + X[num%100/10] + I[num%10]

def main():
    sol = Solution()
    print sol.intToRoman(707) # "DCCVII"
    print sol.intToRoman(94) # XCIV
    print sol.intToRoman(74) # LXXIV
    print sol.intToRoman(1800) # MDCCC

if __name__ == '__main__':
    main()