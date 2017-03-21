# 383 Ransom Note
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = collections.defaultdict(int)
        for c in magazine:
            d[c] += 1
        for c in ransomNote:
            if d[c] == 0:
                return False
            d[c] -= 1
        return True