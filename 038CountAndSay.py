# 038 Count and Say
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 2:
            res = ["1", "11"]
            return res[n-1]
        s = "11"
        for i in xrange(n-2):
            newS = ""
            curr, currLen = s[0], 1
            for j in xrange(1, len(s)):
                if s[j] != curr:
                    newS += str(currLen) + curr
                    curr, currLen = s[j], 1
                else:
                    currLen += 1
            newS += str(currLen) + curr
            s = newS
        return s

def main():
    sol = Solution()
    print sol.countAndSay(1) # "1"
    print sol.countAndSay(2) # "11"
    print sol.countAndSay(4) # "1211"
    print sol.countAndSay(6) # "312211"

if __name__ == '__main__':
    main()