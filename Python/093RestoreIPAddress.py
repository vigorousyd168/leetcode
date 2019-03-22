# 093 Restore IP Address
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        def helper(pre, rest):
            lr = len(rest)
            if lr > 3*(4-len(pre)):
                return
            if lr == 0:
                if len(pre) == 4:
                    res.append('.'.join(pre))
            if lr > 0:
                helper(pre+[rest[0]], rest[1:])
                if lr > 1 and rest[0] != '0':
                    helper(pre+[rest[0:2]], rest[2:])
                    if lr > 2 and int(rest[0:3]) <= 255:
                        helper(pre+[rest[0:3]], rest[3:])
                    else:
                        return
        helper([], s)
        return res

def main():
    sol = Solution()
    print sol.restoreIpAddresses("25525511135") # ["255.255.11.135", "255.255.111.35"]
    print sol.restoreIpAddresses("1111") # ["1.1.1.1"]
    print sol.restoreIpAddresses("255555555") # ["255.55.55.55"]
    print sol.restoreIpAddresses("010010") # ["0.10.0.10", "0.100.1.0"]
if __name__ == '__main__':
    main()