class Solution(object):
    def mergeAlternately(self, word1, word2):
      """
      :type word1: str
      :type word2: str
      :rtype: str
      """
      lenMin, output = len(word1) if len(word1) < len(word2) else len(word2), ''
      for i, j in zip(word1, word2): output += i + j
      return output + word1[lenMin::] + word2[lenMin::]

word1 = '1234  '
word2 = 'qwertyu'
print(Solution.mergeAlternately('', word1, word2))
         
        