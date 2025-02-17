class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for i in range(len(nums)):
            equa = 1
            for j in range(len(nums)): 
                if i != j: equa *= nums[j]
            output.append(equa)
        return output

print(Solution.productExceptSelf('', [1,2,3,4]))
