# 013 Roman to Integer
class Solution(object):
    table = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # do not need a list - can access char in str by indexing: s[i]
        int_value = 0
        left = 0
        right = 0
        for i in range(len(s)-1,-1,-1): # count from len(s)-1 downto 0
            left = self.table[s[i]]
            if left >= right:
                int_value += left
            else:
                int_value -= left
            right = left
        return int_value

def main():
    sol = Solution()
    print sol.romanToInt("DCCVII") # 707
    print sol.romanToInt("XCIV") # 94
    print sol.romanToInt("LXXIV") # 74
    print sol.romanToInt("MDCCC") #1800

if __name__ == '__main__':
    main()