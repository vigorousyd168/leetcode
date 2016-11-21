# 032 Longest Valid Parentheses
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = len(s)
        if ls <= 1:
            return 0
        res = 0
        dp = [0] * ls # the legnth of the longest valid parentheses substring ending at i
        for i in xrange(1, ls):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = 2 if i == 1 else (dp[i-2] + 2)
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + 2 + (0 if i-dp[i-1]-2 < 0 else dp[i-dp[i-1]-2])
                if dp[i] > res:
                    res = dp[i]
        return res
            

def main():
    sol = Solution()
    print sol.longestValidParentheses("") # 0
    print sol.longestValidParentheses("(") # 0
    print sol.longestValidParentheses("()") # 2
    print sol.longestValidParentheses(")(") # 0
    print sol.longestValidParentheses(")((()()(") # 4
    print sol.longestValidParentheses("()()") # 4
    print sol.longestValidParentheses("(())") # 4
    print sol.longestValidParentheses("())()") # 2
    print sol.longestValidParentheses("()(()") # 2
    print sol.longestValidParentheses("()(())") # 6
    print sol.longestValidParentheses(")()())()()(") # 4
if __name__ == '__main__':
    main()