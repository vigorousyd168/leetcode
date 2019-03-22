# 030 Substring with Concatenation of ALl Words
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not words[0]:
            return []
        d = {}
        wordSize = len(words[0])
        l = len(words)
        res = []
        for word in words:
            d[word] = d[word] + 1 if word in d else 1
        for i in xrange(wordSize):
            curr = {}
            start, ll, j = i, 0, i
            while j < len(s) - wordSize + 1:
                k = s[j:j+wordSize]
                if k in d: # good word
                    ll += 1
                    curr[k] = 1 if k not in curr else curr[k] + 1
                    if curr[k] > d[k]:
                        # move start until curr[k] is smaller
                        while curr[k] > d[k]:
                            curr[s[start:start+wordSize]] -= 1
                            ll -= 1
                            start += wordSize
                    if ll == l: # reached goal
                        res.append(start)
                        ll -= 1
                        curr[s[start:start+wordSize]] -= 1
                        start += wordSize # move start once
                else: # bad word
                    curr = {}
                    start = j + wordSize
                    ll = 0
                j += wordSize
        return res

def main():
    sol = Solution()
    print sol.findSubstring("barfoothefoobarman",["foo", "bar"]) # [0, 9]
    print sol.findSubstring("abbbca", ["a", "b", "c", "b"]) # [2]
    print sol.findSubstring("aaaaaaaaaa", ["a", "a", "a"]) # [0,1,2,3,4,5,6,7]
if __name__ == '__main__':
    main()