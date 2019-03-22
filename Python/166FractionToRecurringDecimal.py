# 166 Fraction to Recurring Decimal
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        neg = (numerator < 0) != (denominator < 0)
        numerator = numerator if numerator >= 0 else -numerator
        denominator = denominator if denominator >= 0 else -denominator
        ld = len(str(denominator))
        ln = len(str(numerator))
        idx = ld - 1
        modTable = {}
        # modTable is the table for numbers of the same modular
        pointPos = ln - idx # the position of the decimal point
        digits = []
        recurPos = 0
        # initial
        if ld <= ln:
            res = int((str(numerator))[:ld])
        else:
            pointPos = 1
            res = numerator
            for k in range(0,ld-ln):
                modTable[res] = idx - (ld - 1) + 1
                res = res * 10
                digits.append(0)
                idx += 1
        while 1:
            d = res/denominator
            newRes = res%denominator
            if idx >= ln-1:
                if newRes == 0:
                    digits.append(d)
                    break
            if idx >= ln:
                if res not in modTable.keys():
                    modTable[res] = idx - (ld - 1) + 1 # (ld - 1) is initial idx, +1 for decimal point
                else:
                    recurPos = modTable[res]
                    break
            digits.append(d)
            res = newRes * 10
            if idx < ln-1:
                res += int(str(numerator)[idx+1])
            idx += 1
        result = [str(d) for d in digits]
        if pointPos < len(digits):
            result.insert(pointPos,".")
        if recurPos != 0:
            result.insert(recurPos,"(")
            result.append(")")
        if len(result) >= 2 and result[0] == "0" and result[1] != ".":
            result = result[1:]
        return ("-" if neg else "") + "".join(result)

def main():
    sol = Solution()
    print 1.0/7, sol.fractionToDecimal(1,7)
    print 11.0/3, sol.fractionToDecimal(11,3)
    print 0.0/3, sol.fractionToDecimal(0,3)
    print 1111.0/15, sol.fractionToDecimal(1111,15)
    print 9987.0/3, sol.fractionToDecimal(9987,3)
    print 1.0/5, sol.fractionToDecimal(1,5)
    print 1.0/90, sol.fractionToDecimal(1,90)
    print 1.0/900, sol.fractionToDecimal(1,900)
    print -1.0/900, sol.fractionToDecimal(-1,900)
    print -50.0/8, sol.fractionToDecimal(-50,8)
    print 1.0/333, sol.fractionToDecimal(1,333)
    print 500/10, sol.fractionToDecimal(500,10)
if __name__ == '__main__':
    main()