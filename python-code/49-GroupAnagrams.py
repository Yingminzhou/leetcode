class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        set_dict = dict()
        for i in range(len(strs)):
    		now_str = strs[i]
        	order_str = "".join((lambda x:(x.sort(),x)[1])(list(now_str)))
        	if order_str in set_dict:
        		idx = set_dict[order_str]        		
        		ans[idx].append(now_str)
        	else:
        		ans.append([now_str])
        		set_dict[order_str] = len(ans) - 1
        return ans


s = Solution()
strs = ["eata", "taea", "tan", "ateeee", "nat", "bat"]
ans = s.groupAnagrams(strs)
print ans