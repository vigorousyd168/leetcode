# Game in FF13-2 Time Rift
class Solution(object):
    def tryTimeRift(self, startPos, prefix, visited):
        v = visited[:]
        v[startPos] = True
        p = prefix[:]
        p.append(startPos)
        #print p
        if len(p) == self.n:
            print p
        s = (startPos + self.nums[startPos]) % self.n
        if not v[s]:
            self.tryTimeRift(s, p, v)
        s = (startPos - self.nums[startPos]) % self.n
        s = s + self.n if s < 0 else s
        if not v[s]:
            self.tryTimeRift(s, p, v)
    def timeRift(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.nums = nums
        self.n = len(nums)
        visited = [False] * self.n
        for i in range(self.n):
            self.tryTimeRift(i, [], visited)

def main():
    sol = Solution()
    #sol.timeRift([1,1,2,1,2]) # [3,4,1,2,0]
    #sol.timeRift([2,2,1,3,4,5,1,4,3,3])
    #sol.timeRift([3,1,4,1,3,1,3,1,3,2])
    #sol.timeRift([2,4,4,5,1,1,5,2,1,1])
    sol.timeRift([1,4,5,6,2,6,2,3,4,3,5,5])

if __name__ == '__main__':
    main()