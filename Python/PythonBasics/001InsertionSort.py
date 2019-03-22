# Insertion Sort
class Solution (object):
	def insertionSort(self, A):
		for j in range (1, len(A)):
			key = A[j]
			i = j-1
			# double check the conditions
			while i >= 0 and A[i] > key:
				A[i+1] = A[i]
				i = i-1
			A[i+1] = key
		return A

# Test case
def main():
    sol = Solution()
    print sol.insertionSort([4,4,2,5,1,6])

if __name__ == '__main__':
    main()