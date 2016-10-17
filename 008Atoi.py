class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        digits = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9} # this would be slow :)
        signs = ["+","-"]
        white_space = " "
        ret = 0
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        start = False
        neg = False
        for i in range(len(str)):
            c = str[i]
            if c in digits:
                if not start:
                    start = True
                new_ret = ret * 10 + digits[c]
                # check overflow
                if new_ret > MAX_INT:
                    return MIN_INT if neg else MAX_INT
                ret = new_ret
            elif not start:
                if c in signs:
                    neg = c == signs[1]
                    start = True
                elif c != white_space:
                    return 0 # not startedd but already meet invalid char
            else: # started but meet invalid char
                return ret if not neg else -ret
        # no need to worry about adding "-" to MAX_INT
        return ret if not neg else -ret

def main():
    sol = Solution()
    print "MAX_INT: ", 2**31-1
    print sol.myAtoi("  -09") # -9
    print sol.myAtoi("999999999999999") # MAX_INT
    print sol.myAtoi("-999999999999999") # MIN_INT
    print sol.myAtoi("-0012a42") # -12

if __name__ == '__main__':
    main()