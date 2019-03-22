# 049 Group Anagrams
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for s in strs:
            k = ''.join(sorted(s))
            groups[k] = [s] if k not in groups else groups[k] + [s]
        return groups.values()

def main():
    sol = Solution()
    print sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) # [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
if __name__ == '__main__':
    main()