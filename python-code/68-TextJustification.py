class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        cur_words = list()
        cur_num = 0
        ans = list()
        for i in range(len(words)):
        	word = words[i]
        	if cur_num + len(cur_words) + len(word) <= maxWidth:
        		cur_words.append(word)
        		cur_num += len(word)
        	else:
        		cur_word = self.pad(cur_words, cur_num, maxWidth, False)
        		ans.append(cur_word)
        		cur_words = [word]
        		cur_num = len(word)
        if len(cur_words) > 0:
        	ans.append(self.pad(cur_words, cur_num, maxWidth, True))
        return ans


    def pad(self, cur_words, cur_num, maxWidth, isLeft):
    	cur_word = ""
        if not isLeft and len(cur_words) > 1:
       		avg_space = (maxWidth - cur_num) / (len(cur_words)- 1)
       		more_space = maxWidth - cur_num - avg_space * (len(cur_words) - 1)
       		avg_space_str, more_space_str = "", ""
       		for j in range(avg_space + 1):
      			more_space_str = more_space_str + " "
       			if j < avg_space:
       			    avg_space_str = avg_space_str + " "
       		for j in range(len(cur_words)-1):
       			if j < more_space:
      				cur_word = cur_word + cur_words[j] + more_space_str
     			else:
       				cur_word = cur_word + cur_words[j] + avg_space_str         			
       		cur_word += cur_words[-1]
        else:
        	cur_word = cur_words[0]
        	for j in range(len(cur_words)):
        		if len(cur_word) < maxWidth:
        		    cur_word = cur_word + " " + cur_words[j] 
        	space_num = maxWidth - len(cur_word)
        	for _ in range(space_num):
        		cur_word = cur_word + " "
        return cur_word

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
s = Solution()
print s.fullJustify(words, maxWidth)
