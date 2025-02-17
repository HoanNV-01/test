class Solution(object):
   def canPlaceFlowers(self, flowerbed, n):
      """
      :type flowerbed: List[int]
      :type n: int
      :rtype: bool
      """
      if n == 0: return True
      venv, count_i = flowerbed[:], 0
      for i in range(len(flowerbed)):
         if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) -1 or flowerbed[i+1] == 0): 
            flowerbed[i] = 1
            count_i += 1
      return True if count_i >= n else False

flowerbed = [0,0,1,0,0]
n = 1
print(Solution.canPlaceFlowers('', flowerbed, n))