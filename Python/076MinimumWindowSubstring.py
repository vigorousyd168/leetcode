# 076 Minimum Window Substring
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        kset = set(t)
        ds = {}
        dt = {}
        left = 0
        best_left, best_right = 0, len(s)-1
        valid = False
        for tt in t:
            dt[tt] = 1 if tt not in dt else dt[tt]+1
        for i in xrange(len(s)):
            c = s[i]
            if c in dt:
                ds[c] = 1 if c not in ds else ds[c]+1
                if c in kset and ds[c] >= dt[c]:
                    kset.remove(c)
                    # window big enough?
                    if len(kset) == 0:
                        valid = True
                if valid:
                    while True:
                        if s[left] in ds:
                            if ds[s[left]] == dt[s[left]]:
                                break
                            ds[s[left]] -= 1
                        left += 1
                    if i-left < best_right-best_left:
                        best_left, best_right = left, i
        return "" if not valid else s[best_left:best_right+1]

def main():
    sol = Solution()
    print sol.minWindow("ADOBECODEBANC", "ABC") # "BANC"
    print sol.minWindow("ABCDEFG", "GA") # "ABCDEFG"
    print sol.minWindow("ABCDEFG", "K") # ""
    print sol.minWindow("a", "aa") # ""
    print sol.minWindow("aa", "aa") # "aa"
if __name__ == '__main__':
    main()