# 068 Text Justification
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if len(words) == 0:
            return ["" * maxWidth if maxWidth else 1]
        if maxWidth == 0:
            return [""]
        res = []
        # start is the idx of the first word used in current line
        # used is the length of used characters (including ' ') in current line
        start, used = 0, len(words[0])
        for i in xrange(1, len(words)):
            if used + 1 + len(words[i]) > maxWidth:
                # format current line
                if start == i-1: # one word
                    L = words[start] + ' ' * (maxWidth - used)
                else:
                    nSpaces = maxWidth - used + i-1-start
                    # there are i-start words, i-1-start gaps
                    base, plus = nSpaces / (i-1-start), nSpaces % (i-1-start)
                    L = words[start]
                    for j in xrange(start+1, i):
                        L = L + ' ' * (base + 1) + words[j] if j - (start+1) < plus else L + ' ' * base + words[j]
                res.append(L)
                # start a new line with words[i]
                start, used = i, len(words[i])
            else:
                # add to current line
                used = used + 1 + len(words[i])
        # if all words are used up, fill ' ' till end
        L = words[start]
        for j in xrange(start+1, len(words)):
            L += ' ' + words[j]
        L += ' ' * (maxWidth - used)
        res.append(L)
        return res


def main():
    sol = Solution()
    print sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16) # 2
    # ["This    is    an", "example  of text", "justification.  "]
    print sol.fullJustify([""], 0) # [""]
    print sol.fullJustify([""], 5) # ["     "]
    print sol.fullJustify([], 5) # ["     "]
    print sol.fullJustify(["a"], 5) # ["a    "]
    print sol.fullJustify(["a"], 0) # ?
    print sol.fullJustify(["a","b"], 1) # ["a", "b"]
    print sol.fullJustify(["What","must","be","shall","be."], 12) # ["What must be","shall be.   "]
if __name__ == '__main__':
    main()