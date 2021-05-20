class Solution:
    def solve(self, nums):
        index_of_ones = []
        for i in range(0,len(nums)):
            if nums[i] == 1:
                index_of_ones.append(i)
        for j in range(0,len(index_of_ones)-1):
            if (index_of_ones[j+1] - index_of_ones[j]) > 1:
                return False
                break
        else:
            return True