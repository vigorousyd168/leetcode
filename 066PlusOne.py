class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            digits = [0]
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits

def main():
    sol = Solution()
    print sol.plusOne([]) # [1]
    print sol.plusOne([0]) # [1]
    print sol.plusOne([9,9,9,9]) # [1,0,0,0,0]

if __name__ == '__main__':
    main()