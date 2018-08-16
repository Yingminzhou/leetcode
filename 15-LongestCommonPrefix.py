class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
        	return ""
        preStr = strs[0]
        for i in range(1, len(strs)):
        	nowStr = strs[i]
        	if preStr == "":
        		break
        	preStr = self.longestCommonPrefixTwo(preStr, nowStr)
        return preStr
        


    def longestCommonPrefixTwo(self, str1, str2):
    	"""
        :type str1: str1 
        :type str2: str2
        :rtype: str
        """
    	i = 0
    	while i < len(str1) and i < len(str2):
    		if str1[i] == str2[i]:
    			i += 1
    		else:
    			break
    	i -= 1
    	if i >= 0:
    		return str1[:i+1]
    	else:
    		return ""