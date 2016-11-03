# 091 Decode Ways
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0:
            return 0
        if ord(s[0]) <= ord('0') or ord(s[0]) > ord('9'): # invalid
            return 0
        if l == 1:
            return 1
        sec = 1
        if s[1] == '0':
            if not (s[0] == '1' or s[0] == '2'):
                return 0
        elif ord(s[1]) > ord('0') and ord(s[1]) < ord('7'):
            if s[0] == '1' or s[0] == '2':
                sec = 2
        elif ord(s[1]) >= ord('7') and ord(s[1]) <= ord('9'):
            if s[0] == '1':
                sec = 2

        dp = [1] + [sec] + [0] * (l-2)
        for i in range(2, l):
            if s[i] == '0':
                if ord(s[i-1]) > ord('2') or ord(s[i-1]) <= ord('0'):
                    return 0 # invalid
                dp[i] = dp[i-2]
            elif ord(s[i]) > ord('0') and ord(s[i]) < ord('7'):
                dp[i] = (dp[i-1] + dp[i-2]) if s[i-1] == '1' or s[i-1] == '2' else dp[i-1]
            elif ord(s[i]) >= ord('7') and ord(s[i]) <= ord('9'):
                dp[i] = (dp[i-1] + dp[i-2]) if s[i-1] == '1' else dp[i-1]
            else:
                return 0 # invalid
        return dp[-1]

def main():
    sol = Solution()
    print sol.numDecodings("8716238576102215") # 20
    print sol.numDecodings("0") # 0
    print sol.numDecodings("110") # 1
    print sol.numDecodings("100") # 0
    print sol.numDecodings("101") # 1
    print sol.numDecodings("301") # 0
if __name__ == '__main__':
    main()