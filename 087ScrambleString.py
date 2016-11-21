# 087 Scramble String
class Solution(object):
    def __init__(self):
        self.cache = {}
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        if (s1,s2) in self.cache.keys():
            return self.cache[(s1,s2)]
        l = len(s1)
        counts = {}
        for i in xrange(l):
            counts[s1[i]] = 1 if s1[i] not in counts.keys() else counts[s1[i]] + 1
            counts[s2[i]] = -1 if s2[i] not in counts.keys() else counts[s2[i]] - 1
        for k in counts.keys():
            if counts[k] != 0:
                self.cache[(s1,s2)] = False
                return False
        for i in xrange(1, l): # at least one child, at most l-1 children in subtree
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:],s2[i:])) \
            or (self.isScramble(s1[:i], s2[l-i:]) and self.isScramble(s1[i:],s2[:l-i])):
                self.cache[(s1,s2)] = True
                return True
        self.cache[(s1,s2)] = False
        return False

def main():
    sol = Solution()
    print sol.isScramble("a", "a") # True
    print sol.isScramble("ab", "ba") # True
    print sol.isScramble("abcde", "daecb") # False
    print sol.isScramble("", "") # True
    print sol.isScramble("abc", "acb") # True
if __name__ == '__main__':
    main()