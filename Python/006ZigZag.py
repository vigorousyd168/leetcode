# 006 ZigZag Conversion
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # corner cases
        if numRows < 1:
            return "error"
        if numRows == 1:
            return s
        ret = ""
        length = len(s)
        step = 2 * numRows - 2
        for i in range(numRows):
            if i == 0 or i == (numRows - 1):
                idx = i
                while (idx < length):
                    ret = ret + s[idx]
                    idx += step
            else:
                idx = i
                while (idx < length):
                    ret = ret + s[idx]
                    if (idx + step - 2*i <= length - 1): # consider the case when s ends before reaching this index
                        ret = ret + s[idx + step - 2*i]
                    idx += step
        return ret

def main():
    sol = Solution()
    print sol.convert("", 3) # empty string
    print sol.convert("PAYPALISHIRING", 3) # PAHNAPLSIIGYIR
    print sol.convert("PAYPALISHIRING", 1) # PAYPALISHIRING
    print sol.convert("ABCD", 3) # ABDC
    print sol.convert("GG", 3) # GG
if __name__ == '__main__':
    main()