class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        sim_path = list()
        now_path = ""
        for i in range(len(path)):
        	cur = path[i]
        	if cur == "/":
        		if len(now_path) > 0:
        			if now_path == '..':
     					if len(sim_path) > 0:
        					sim_path = sim_path[:-1]
        			elif now_path != '.':
        				sim_path.append(now_path)
        			now_path = ""
        	else:
        		now_path += cur
        if len(now_path) > 0:
        	if now_path == '..':
     			if len(sim_path) > 0:
        			sim_path = sim_path[:-1]
        	elif now_path != '.':
        		sim_path.append(now_path)
        return "/" + "/".join(sim_path)

path = "/.../a/..a/c"
s = Solution()
print s.simplifyPath(path)
