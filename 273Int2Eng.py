# 273 Integer to English Words
import time
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        myDict = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty", # Forty
            50: "Fifty", # Fifty
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety", # Ninety
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion",
        }
        if num == 0:
            return myDict[0]
        result = []
        # billion
        if num/1000000000 != 0:
            result.append(myDict[num/1000000000])
            result.append(myDict[1000000000])
        num = num%1000000000
        # million
        if num/1000000 != 0:
            result.append(self.numberToWords(num/1000000))
            result.append(myDict[1000000])
        num = num%1000000
        # thousand
        if num/1000 != 0:
            result.append(self.numberToWords(num/1000))
            result.append(myDict[1000])
        num = num%1000
        # hundred
        if num/100 != 0:
            result.append(self.numberToWords(num/100))
            result.append(myDict[100])
        num = num%100
        # other
        if num != 0:
            if num/10 <= 1:
                result.append(myDict[num])
            else:
                for d in range(2,10):
                    if num/10 == d:
                        result.append(myDict[d*10])
                        if num%10 != 0:
                            result.append(myDict[num%10])
        return " ".join(result)

def main():
    sol = Solution()
    start_time = time.clock()
    print sol.numberToWords(0) # Zero
    print sol.numberToWords(1) # One
    print sol.numberToWords(30) # Thirty
    print sol.numberToWords(100000) # One Hundred Thoudsand
    print sol.numberToWords(123) # "One Hundred Twenty Three"
    print sol.numberToWords(12345) # "Twelve Thousand Three Hundred Forty Five"
    print sol.numberToWords(1234567) # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    print sol.numberToWords(2147483647) # "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven"
    print("--- %s seconds ---" % (time.clock() - start_time))

if __name__ == '__main__':
    main()