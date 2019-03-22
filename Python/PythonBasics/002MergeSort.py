# Merge Sort
import sys # using sys.maxint
class Solution(object):
	L = []
	R = []
	def mergeSort(self, A, p, r):
		if p < r:
			q = (p + r)/2 # should be int
			self.mergeSort(A, p, q)
			self.mergeSort(A, q+1, r)
			self.merge(A, p, q, r)
		return A
	def merge(self, A, p, q, r):
		# copy to a new array self.L
		self.L = A[p:q+1]
		self.L.append(sys.maxint)
		# copy to a new array self.R
		self.R = A[q+1:r+1]
		self.R.append(sys.maxint)
		l_idx = 0
		r_idx = 0
		for k in range (p, r+1):
			if self.L[l_idx] < self.R[r_idx]:
				A[k] = self.L[l_idx]
				l_idx += 1
			else:
				A[k] = self.R[r_idx]
				r_idx += 1
		return A

# Test case
def main():
    sol = Solution()
    print sol.mergeSort([4,4,2,5,1,6], 0, 5)

if __name__ == '__main__':
    main()
