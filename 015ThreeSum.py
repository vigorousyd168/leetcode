# 015 Three Sum
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # step 1: sort - O(nlgn)
        # sorted list (we don't need the original any more then)
        l = sorted(nums)
        triplet_list = []
        triplet = []
        
        # step 2: create dict - O(n)
        table = {}
        for i in range(0, len(l)):
            if l[i] not in table:
                table[l[i]] = 1
            else:
                table[l[i]] += 1 # here we cannot use ++/--
                
        # step 3: loop and find - O(n^2)
        # make sure the numbers in the triplet are non-decreasing
        for i in range(0, len(l)):
            table[l[i]] -= 1
            for j in range(i+1, len(l)):
                # account for duplicate elements
                if table[l[j]] == 0:
                    continue
                table[l[j]] -= 1
                if (-l[i]-l[j] >= l[j]) and (-l[i]-l[j] in table) and (table[-l[i]-l[j]] > 0):
                    candidate = [l[i],l[j],-l[i]-l[j]]
                    if (len(triplet_list)) == 0:
                        triplet_list.append(candidate) # list has no add() method, append() !!!
                    # WA - only comparing (using !=) with the last in list is NOT sufficient
                    elif (triplet_list[-1][0] < candidate[0]) or (triplet_list[-1][1] < candidate[1]):
                        triplet_list.append(candidate)
                table[l[j]] += 1
            table[l[i]] += 1
        
        return triplet_list

def main():
    sol = Solution()
    print sol.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])

if __name__ == '__main__':
    main()
