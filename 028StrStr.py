# 028 Implement strStr()
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        k = len(needle)
        if k == 0:
            return 0
        for i in xrange(len(haystack)-k+1):
            for kk in xrange(k):
                if haystack[i+kk] != needle[kk]:
                    break
                if kk == k-1:
                    return i
        return -1

def main():
    sol = Solution()
    print sol.strStr("abc", "c") # 2
    print sol.strStr("", "") # 0
    print sol.strStr("", "a") # -1
    print sol.strStr("aabc", "abc") # 1
if __name__ == '__main__':
    main()