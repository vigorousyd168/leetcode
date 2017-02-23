# 022 Longest Increasing Subsequence
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        def helper(totalL, totalR, n):
            res = []
            if totalL == n and totalR == n:
                return [""]
            if totalL < n:
                res += ["(" + p for p in helper(totalL+1, totalR, n)]
            if totalR < totalL:
                res += [")" + p for p in helper(totalL, totalR+1, n)]
            return res
        return helper(0, 0, n)

def main():
    sol = Solution()
    print sol.generateParenthesis(1) # ["()"]
    print sol.generateParenthesis(3) # ["((()))", ... , "()()()"]
    print sol.generateParenthesis(0) # []
if __name__ == '__main__':
    main()