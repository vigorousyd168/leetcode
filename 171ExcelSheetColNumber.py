# 171 Excel Sheet Column Number
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = 26
        letters = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
        result = 0
        v = 1
        for l in s[::-1]:
            result += letters[l] * v
            v *= base
        return result
def main():
    sol = Solution()
    print sol.titleToNumber("A") # 1
    print sol.titleToNumber("Z") # 26
    print sol.titleToNumber("AA") # 27
    print sol.titleToNumber("YZ") # 676
    print sol.titleToNumber("AAA") # 703

if __name__ == '__main__':
    main()