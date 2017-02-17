# 467 Unique Substrings In Wraparound String
class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        n = len(p)
        if n == 0:
            return 0
        # d[k] is the maximum length of good substring ending with k
        d = {k: 0 for k in "abcdefghijklmnopqrstuvwxyz"}
        d[p[0]] = 1
        res, count = 1, 1
        for i in xrange(1, n):
            count = (count + 1) if (ord(p[i]) - ord(p[i-1]) == 1 or (p[i] == 'a' and p[i-1] == 'z')) else 1
            if count > d[p[i]]: # never counted before
                res += count - d[p[i]]
                d[p[i]] = count               
        return res

def main():
    sol = Solution()
    print sol.findSubstringInWraproundString("zbb") # 2
    print sol.findSubstringInWraproundString("zabzabc") # 10
    print sol.findSubstringInWraproundString("a") # 1
    print sol.findSubstringInWraproundString("aa") # 1
    print sol.findSubstringInWraproundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") # 1027
if __name__ == '__main__':
    main()
