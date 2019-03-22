# 400 Nth Digit
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 2^32 < 10^10
        # pre: number of integers that have <k digits
        pre = 0
        digit_count = 0
        for k in range(1, 10):
            # there are 9*10**(k-1) numbers that have k digits
            num_k_digits = 9*10**(k-1)
            if digit_count < n and n <= digit_count + k*num_k_digits:
                # the integer number should have k digits
                # the first integer number that has k digits is 10^(k-1)
                # this integer number is the {(n-digit_count-1)/k+1}th integer number that has k digits
                int_num = (n - digit_count - 1)/k + 1 + pre
                # note: we return an integer, not a string
                d = str(int_num)[n - digit_count - (n-digit_count-1)/k * k - 1]
                return int(d)
            pre += num_k_digits
            digit_count += k*num_k_digits

def main():
    sol = Solution()
    #print sol.findNthDigit(2) # 2
    #print sol.findNthDigit(11) # 0
    #print sol.findNthDigit(12) # 1
    #print sol.findNthDigit(13) # 1
    #print sol.findNthDigit(14) # 1
    #print sol.findNthDigit(15) # 2
    print sol.findNthDigit(1000) # 3

if __name__ == '__main__':
    main()
