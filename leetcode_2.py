class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1) < len(str2): str1, str2 = str2, str1
        while str2:
            lenMin = len(str2)
            if str1[:lenMin] == str2: return ''
            elif str1[:lenMin] == str2: str1 = str1.replace(str2, '')
            else: return str2
            str2, str1 = str1, str2
        return str1