class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        wcDict = self.prepareDict(words)
        wordLen = len(words[0])
        wordNum = len(words)
        matchIdxList = []
        for i in range(wordLen):
            nowDict = dict()
            matchCnt = 0
            curIdx = i
            for j in range(i,len(s)-wordLen+1,wordLen):
                nowWord = s[j:j+wordLen]
                if nowWord in wcDict:
                    cnt = 1
                    if nowWord in nowDict:
                        cnt += nowDict[nowWord]
                    nowDict[nowWord] = cnt
                    if cnt <= wcDict[nowWord]:
                        matchCnt += 1
                    else:
                        while True:
                            tmp = s[curIdx: curIdx + wordLen]
                            nowDict[tmp] = nowDict[tmp] - 1
                            curIdx += wordLen
                            if tmp == nowWord:
                                break
                            else:
                                matchCnt -= 1
                    if matchCnt == wordNum:
                        matchIdxList.append(curIdx)
                        tmp = s[curIdx: curIdx + wordLen]
                        nowDict[tmp] = nowDict[tmp] - 1
                        curIdx += wordLen
                        matchCnt -= 1
                else:
                    nowDict = dict()
                    matchCnt = 0
                    curIdx = j + wordLen
        return matchIdxList



    def prepareDict(self, words):
        wcDict = dict()
        for i in range(len(words)):
            cnt = 1
            if words[i] in wcDict:
                cnt += wcDict[words[i]]
            wcDict[words[i]] = cnt
        return wcDict

sl = Solution()
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]

arr = sl.findSubstring(s, words)
print arr