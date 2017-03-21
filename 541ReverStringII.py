# 542 Reverse String II
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 1:
            return s
        left, right = s[:len(s) / (2*k) * 2 * k], s[len(s) / (2*k) * 2 * k:]
        l = []
        for i in xrange(len(left)):
            m = i / k
            if m % 2 == 0:
                l.append(s[2*k*m+k-1-i])
            else:
                l.append(s[i])
        end = right[::-1] if len(right) <= k else right[:k][::-1] + right[k:]
        return ''.join(l) + end