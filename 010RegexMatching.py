class Solution(object):
    def singleMatch(self, s, p):
        return s == p or p == "."
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

def main():
    sol = Solution()
    print sol.isMatch("aa","a") # False
    print sol.isMatch("aa","aa") # True
    print sol.isMatch("aa","a*") # True
    print sol.isMatch("aaa","a.*a") # True
    print sol.isMatch("b",".*b") # True
    print sol.isMatch("abcc","abc*cc")

if __name__ == '__main__':
    main()