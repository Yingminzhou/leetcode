class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return "()"
        i = 1
        parentSet = set()
        parentSet.add("()")
        while i < n:
            nowSet = set()
            for parent in parentSet:
                nowStr = "(" + parent + ")"
                nowSet.add(nowStr)
                nowStr = "()" + parent
                nowSet.add(nowStr)
                for j in range(len(parent), 1, -1):
                    if parent[j-1] == "(":
                        nowStr = "(" + parent[:j-1] + ")" + parent[j-1:]
                        nowSet.add(nowStr)
            parentSet = nowSet
            i+=1
        return list(parentSet)


s = Solution()
n = 3
print s.generateParenthesis(n)