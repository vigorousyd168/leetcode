# 165 Compare Version Numbers
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1 = [int(s) for s in version1.split('.')]
        l2 = [int(s) for s in version2.split('.')]
        for i in xrange(min(len(l1), len(l2))):
            if l1[i] > l2[i]:
                return 1
            elif l1[i] < l2[i]:
                return -1
        if len(l1) == len(l2):
            return 0
        elif len(l1) > len(l2):
            return 0 if set(l1[len(l2):]) == set([0]) else 1
        else:
            return 0 if set(l2[len(l1):]) == set([0]) else -1

def main():
    sol = Solution()
    print sol.compareVersion("0.1", "1.0") # -1
    print sol.compareVersion("0.01", "0.1") # 0
    print sol.compareVersion("1.1", "1.2") # -1
    print sol.compareVersion("1.1.2", "1.1.2.3") # -1
    print sol.compareVersion("1.1.2", "1.2") # -1
    print sol.compareVersion("1.0", "1") # 0
if __name__ == '__main__':
    main()