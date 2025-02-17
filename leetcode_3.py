class Solution(object):
   def kidsWithCandies(self, candies, extraCandies):
      """
      :type candies: List[int]
      :type extraCandies: int
      :rtype: List[bool]
      """
      kid_GetCandies = [(i + extraCandies) for i in candies] # Số kẹo mỗi đứa trẻ nhận 
      min_Max = [(True if i > max(candies) else False) for i in kid_GetCandies]
      
      return min_Max
