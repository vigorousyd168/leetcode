# 010 Regular Expression Matching
class Solution(object):
    def singleMatch(self, s, p):
        return s == p or p == '.'
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls, lp = len(s), len(p)
        dp = [[False] * (ls+1) for _ in xrange(lp+1)]
        # init first row (p = "")
        dp[0][0] = True
        # init first col (s = "")
        for i in xrange(2, lp+1):
            dp[i][0] = dp[i-2][0] and p[i-1] == '*'
        # inner table
        for i in xrange(1, lp+1):
            for j in xrange(1, ls+1):
                if p[i-1] == '*':
                    dp[i][j] = i >= 2 and dp[i-2][j] or (dp[i][j-1] and (p[i-2] == s[j-1] or p[i-2] == '.'))
                else:
                    dp[i][j] = (p[i-1] == s[j-1] or p[i-1] == '.') and dp[i-1][j-1]
        return dp[-1][-1]


    def isMatch_recursive(self, s, p): # TLE
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (len(s) > 0 and self.singleMatch(s[0], p[0]) and self.isMatch(s[1:], p))
        else:
            return len(s) > 0 and self.singleMatch(s[0], p[0]) and self.isMatch(s[1:], p[1:])


def main():
    sol = Solution()
    print sol.isMatch("", "a*") # True
    print sol.isMatch("", "a") # False
    print sol.isMatch("aa","a") # False
    print sol.isMatch("aa","aa") # True
    print sol.isMatch("aa","a*") # True
    print sol.isMatch("aaa","a.*a") # True
    print sol.isMatch("b",".*b") # True
    print sol.isMatch("abcc","abc*cc") # True
    print sol.isMatch("bbbbbc", "b*b*c") # True
    print sol.isMatch("ab", ".*c") # False
    print sol.isMatch("aaa", "ab*a*c*a") # True
    print sol.isMatch("aaca", "ab*a*c*a") # True

if __name__ == '__main__':
    main()