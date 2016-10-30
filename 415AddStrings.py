# 415 Add Strings
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            return self.addStrings(num2, num1)
        res = []
        c = 0
        for i in xrange(len(num1)):
            s = (int(num1[~i]) + int(num2[~i]) + c) if i < len(num2) else (int(num1[~i]) + c)
            s, c = s % 10, s > 9
            res.append(str(s))
        if c:
            res.append("1")
        return "".join(res[::-1])
def main():
    sol = Solution()
    print sol.addStrings([0], [0]) # "0"
    print sol.addStrings([5],[5]) # "10"
    print sol.addStrings([9],[9,9]) # "108"

if __name__ == '__main__':
    main()