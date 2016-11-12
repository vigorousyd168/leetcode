# 392 Is Subsequence
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        idx, ls, lt = 0, len(s), len(t)
        for i in xrange(ls):
            while idx <= lt - 1:
                if t[idx] != s[i]:
                    idx += 1
                else:
                    break
            if idx >= lt:
                return False
            idx += 1
        return True

def main():
    sol = Solution()
    print sol.isSubsequence("abc", "ahbgdc") # True
    print sol.isSubsequence("aaa", "aab") # False
    print sol.isSubsequence("", "a") # True
if __name__ == '__main__':
    main()