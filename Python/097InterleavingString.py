# 097 Interleaving String
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        if l3 == 0:
            return True
        dp = [[False] * (l2+1) for _ in xrange(l1+1)]
        dp[0][0] = True
        # first row
        for j in xrange(1, l2+1):
            dp[0][j] = s3[:j] == s2[:j]
        for i in xrange(1, l1+1): # i: length of s1 substring
            dp[i][0] = s3[:i] == s1[:i]
            for j in xrange(1, l2+1): # j: length of s2 substring
                dp[i][j] = (s3[i+j-1] == s1[i-1] and dp[i-1][j]) or (s3[i+j-1] == s2[j-1] and dp[i][j-1])
            if sum(dp[i]) == 0:
                return False
        return dp[-1][-1]
    def isInterleave_2(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        if l3 == 0:
            return True
        dp = [[False] * (l1+1) for _ in xrange(l3+1)]
        dp[0][0] = True
        if l1 > 0:
            dp[1][1] = s3[0] == s1[0]
        if l2 > 0:
            dp[1][0] = s3[0] == s2[0]
        for i in xrange(1, l3+1): # i: length of s3 substring
            if i <= l2:
                dp[i][0] |= s3[:i] == s2[:i]
            for j in xrange(max(1,i-l2), min(i,l1)+1): # j: length of s1 substring
                #print i,j,dp[i][j]
                if j >= 1:
                    dp[i][j] |= s3[i-1] == s1[j-1] and dp[i-1][j-1]
                if i-j >= 1: # i-j: length of s2 substring
                    dp[i][j] |= s3[i-1] == s2[i-j-1] and dp[i-1][j]
            if sum(dp[i]) == 0:
                return False
        return True
    def isInterleave_recursive(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        if l3 == 0:
            return True
        if l3 == 1:
            return s3[0] == s1[0] if l1 == 1 else s3[0] == s2[0]
        res = False
        if l1 > 0:
            res |= s3[-1] == s1[-1] and self.isInterleave(s1[:-1],s2,s3[:-1])
        if l2 > 0:
            res |= s3[-1] == s2[-1] and self.isInterleave(s1,s2[:-1],s3[:-1])
        return res

def main():
    sol = Solution()
    print sol.isInterleave("a","b","ab") # True
    print sol.isInterleave("a","b","ba") # True
    print sol.isInterleave("aabcc","dbbca","aadbbcbcac") # True
    print sol.isInterleave("aabcc","dbbca","aadbbbaccc") # False
    print sol.isInterleave("","","") # True
    print sol.isInterleave("","abc","abc") # True
if __name__ == '__main__':
    main()