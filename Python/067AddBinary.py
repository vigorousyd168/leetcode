class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # make sure len(a) >= len(b)
        if len(a) < len(b):
            return self.addBinary(b,a)
        cc = [int(bin) for bin in a]
        bb = [int(bin) for bin in b]
        for i in range(len(cc)):
            if i <= len(bb) - 1:
                cc[~i] += bb[~i]
            if cc[~i] >= 2:
                cc[~i] -= 2
                if i < len(cc) - 1:
                    cc[~(i+1)] += 1
                else:
                    cc.insert(0,1)
            else: # no carry
                # if b already ends, return early
                if i > len(bb) - 1:
                    break
        c = ""
        for i in range(len(cc)):
            c += str(cc[i])
        return c
        

def main():
    sol = Solution()
    print sol.addBinary("", "1001") # "1001"
    print sol.addBinary("0", "1001") # "1001"
    print sol.addBinary("1", "111") # "1000"

if __name__ == '__main__':
    main()