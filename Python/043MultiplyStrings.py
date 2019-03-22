class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # i,j -> product placed at position (i+j+1,i+j) (counting from right)
        # length: l1, l2 -> l1+l2-1 or l1+l2
        ret = []
        for k in range(len(num1)+len(num2)):
            ret.append(0)
        for i in range(len(num1)):
            for j in range(len(num2)):
                p = int(num1[~i]) * int(num2[~j]) # LSB on the right!!!
                ret[~(i+j)] += p % 10
                ret[~(i+j+1)] += p / 10
        result = ""
        for i in range(len(ret)):
            # process carries
            if ret[~i] >= 10:
                ret[~(i+1)], ret[~i] = ret[~(i+1)]+ret[~i]/10, ret[~i]%10
            result = result + str(ret[~i]) # reversed
        for i in range(len(ret)):
            if result[~i] != "0":
                return result[~i::-1]
        return "0"
        
def main():
    sol = Solution()
    print 4*5
    print sol.multiply("4", "5")
    print 22222222222222*33333333333333
    print sol.multiply("22222222222222","33333333333333")
    print 9133*0
    print sol.multiply("9133", "0")

if __name__ == '__main__':
    main()