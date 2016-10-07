# 014 Longest Common Prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = ""
        if len(strs) == 0:
            return ret
        minLen = len(strs[0])
        if minLen == 0:
            return ret
        for str in strs:
            if len(str) < minLen:
                minLen = len(str)
        for i in range(0, minLen):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i] # return immediately
        # the str with min length is the longest common prefix
        return strs[0][:minLen]
def main():
    sol = Solution()
    print sol.longestCommonPrefix(["aa", "aab"]) # aa
    print sol.longestCommonPrefix(["aab", "aa"]) # aa
    print sol.longestCommonPrefix(["", "ab"]) # empty string
    print sol.longestCommonPrefix(["abc", "ab", "abcd"]) # ab
if __name__ == '__main__':
    main()