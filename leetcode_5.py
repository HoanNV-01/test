# Đảo ngược vị trí của nguyên âm, giữ nguyên vị trí của các kí tự khác đảm bảo đúng vị trí
class Solution(object):
   def reverseVowels(self, s):
      """
      :type s: str
      :rtype: str
      """
      nguyen_am = []
      du_phong = []
      for i in list(s):
         if i in "ueoaiUEOAI": 
            nguyen_am.append(i)
            du_phong.append('')
         else: du_phong.append(i)
      b = nguyen_am[::-1]
      for i in range(0, len(du_phong) - 1):
         if(du_phong[i] == ''):
            du_phong[i] = b[0]
            b.remove(b[0])
      return(''.join(du_phong))