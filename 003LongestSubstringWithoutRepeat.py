# 003 Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        # start: start position of currently considered substring
        res, start = 0, 0
        for i in xrange(len(s)):
            c = s[i]
            if c in d and d[c] >= start:
                start = d[c] + 1
            else:
                res = i-start+1 if i-start+1 > res else res
            d[c] = i
        return res
def main():
    sol = Solution()
    print sol.lengthOfLongestSubstring("abcabcbb") # 3
    print sol.lengthOfLongestSubstring("bbbbb") # 1
    print sol.lengthOfLongestSubstring("pwwkew") # 3
    print sol.lengthOfLongestSubstring("dvdf") # 3
    print sol.lengthOfLongestSubstring("tmmzuxt") # 5
    print sol.lengthOfLongestSubstring("bbtablud") # 6
if __name__ == '__main__':
    main()