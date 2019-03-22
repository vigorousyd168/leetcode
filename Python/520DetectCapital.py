# 520 Detect Capital
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        l = len(word)
        if l == 0:
            return True
        prev = word[0].isupper()
        for i in xrange(1, l):
            curr = word[i].isupper()
            if prev and not curr and i != 1:
                return False
            if not prev and curr:
                return False
            prev = curr
        return True