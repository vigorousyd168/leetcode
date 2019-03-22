# 372 Super Power
class Solution(object):
    def superPow(self, a, b): # 45ms
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        # Euler's phi function: l = phi(1337) = 6 * 190 = 1140
        l, c, bb, base = 1140, 1337, 0, 1
        # reduce b to bb
        for d in b[::-1]:
            bb = (bb + d*base) % l
            base = base*10 % l
        result = 1
        a = a % c
        for i in xrange(bb):
            result = result*a % c
        return result

    def superPow1(self, a, b): # 100ms
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if a == 1:
            return 1
        modList = []
        modListComplete = False
        l, idx, c, base, r = 0, -1, 1337, 1, 1
        for d in b[::-1]:
            if modListComplete:
                idx = (idx + d*base) % l
            else:
                for i in xrange(d*base):
                    r = r*a % c
                    if r not in modList:
                        modList.append(r)
                        l += 1
                        idx += 1
                    else:
                        modListComplete = True
                        idx = (idx + d*base - i) % l
                        break
            base = (base * 10 % l) if modListComplete else (base * 10)
        return modList[idx]

def main():
    sol = Solution()
    print sol.superPow(2,[3]) # 8
    print sol.superPow(2, [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]) # 862
    print sol.superPow(1337, [9,9,9,9,9,9,9,9,9,9,9,9]) # 0

if __name__ == '__main__':
    main()