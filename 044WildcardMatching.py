# 044 Wildcard Matching
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls, lp = len(s), len(p)
        idx_s, idx_p = 0, 0
        last_wildcard, last_idx_s = -1 , -1
        while idx_s < ls:
            if idx_p < lp and (p[idx_p] == s[idx_s] or p[idx_p] == '?'):
                idx_s, idx_p = idx_s + 1, idx_p + 1
            elif idx_p < lp and p[idx_p] == '*':
                last_wildcard, last_idx_s = idx_p, idx_s
                idx_p += 1
            elif last_wildcard != -1:
                idx_p, idx_s = last_wildcard + 1, last_idx_s + 1
                last_idx_s = last_idx_s + 1
            else:
                return False
        # handle left '*'s in p
        while idx_p < lp and p[idx_p] == '*':
            idx_p += 1
        return idx_p == lp

    def isMatch_1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls, lp = len(s), len(p)
        if lp - p.count('*') > ls:
            return False
        dp = [True] + [False] * ls
        for i in xrange(1, lp+1):
            if p[i-1] != '*':
                for j in xrange(ls, 0, -1): # right to left
                    dp[j] = dp[j-1] and (p[i-1] == s[j-1] or p[i-1] == '?')
            else: # is '*'
                for j in xrange(1, ls+1): # still left to right
                    dp[j] = dp[j] or dp[j-1]
            dp[0] = p[i-1] == '*' and dp[0]
        return dp[-1]
    def isMatch_2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls, lp = len(s) + 1, len(p) + 1
        if lp - p.count('*') > ls:
            return False
        dp = [False] * ls
        prev = [False] * ls
        # init first row (p = "")
        dp[0] = True # others all False
        # inner table
        for i in xrange(1, lp):
            prev = dp[:]
            dp[0] = p[i-1] == '*' and prev[0]
            for j in xrange(1, ls):
                if p[i-1] != '*':
                    dp[j] = prev[j-1] if (p[i-1] == s[j-1] or p[i-1] == '?') else False
                else: # is '*'
                    dp[j] = prev[j] or dp[j-1]
        return dp[-1]

def main():
    sol = Solution()
    print sol.isMatch("", "a*") # False
    print sol.isMatch("", "a") # False
    print sol.isMatch("aa","a") # False
    print sol.isMatch("aa","aa") # True
    print sol.isMatch("aa","a*") # True
    print sol.isMatch("ab", "*a") # False
    print sol.isMatch("aaa","a*a") # True
    print sol.isMatch("b","*b") # True
    print sol.isMatch("abcc","ab*cc") # True
    print sol.isMatch("bbbbbc", "b*b*c") # True

if __name__ == '__main__':
    main()