# 459 Repeated Substring Pattern
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        for i in xrange(2, l+1):
            if l % i == 0:
                d = l/i
                r = True
                for j in xrange(1, i):
                    if s[j*d:(j+1)*d] != s[:d]:
                        r = False
                        break
                if r:
                    return True
        return False