# 050 Pow
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # note: type of x is float
        # note: overflow
        # idea: use intermediate results
        if n == 0:
            return 1.0
        if n < 0:
            n = 0-n
            if x == 0:
                return 0.0 # avoid division by zero
            else:
                x = 1.0/x
        MAX_INT = 2**31-1
        THRESHOLD = 0.01
        bit_array = bin(n)[2:] # key step here!!!
        k = len(bit_array)-1
        # compute the intermediate results
        temp = x
        inter = [temp]
        for i in range(k):
            # 1,2...k
            new_temp = temp * temp
            # avoid division by zero error
            if temp == 0:
                return 0.0
            if (new_temp/temp - temp > THRESHOLD) or (new_temp/temp - temp < -THRESHOLD):
                #print "overflow 1"
                return MAX_INT
            inter.append(new_temp)
            temp = new_temp
        # now inter should have k+1 numbers: [x^(2^kk), for kk = 0,1...k]
        result = 1.0
        for i in range(k+1):
            if bit_array[k-i] == '1':
                new_result = result * inter[i]
                if (new_result/result - inter[i] > THRESHOLD) or (new_result/result - inter[i] < -THRESHOLD):
                    #print "overflow 2"
                    return MAX_INT
                result = new_result
        # special handling for integer in Python
        if result > MAX_INT or result < -MAX_INT-1:
            return MAX_INT
        return result
        
def main():
    sol = Solution()
    print "2^31-1 is: ", 2**31-1
    print sol.myPow(1.0, 0) # 1.0
    print sol.myPow(2.0, 1) # 2.0
    print sol.myPow(3.0, 3) # 27
    print sol.myPow(3.89707, 2) # 15.18715
    print sol.myPow(2.0, 31) # 2**31 - 1
    print sol.myPow(2.0, -2) # 0.25
    print sol.myPow(0.0001, 2222222) # 0
    # the wrong answer indicates that when n < 0, we do need to compute the intermediate inverse
    # taking inverse at last can lead to unexpected overflow
    print sol.myPow(2.00000, -2147483648) # 0.00000
if __name__ == '__main__':
    main()