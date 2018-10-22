class Solution(object):

    seq_dict = dict()

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        now_seq = "1"
        if n == 1:
            self.seq_dict[n] = now_seq
        if n in self.seq_dict:
            return self.seq_dict[n]
        pre_seq = now_seq
        for i in range(1, n):
            now_seq = self.countAndSayNext(pre_seq)
            self.seq_dict[i+1] = now_seq
            pre_seq = now_seq
        return now_seq

    def countAndSayNext(self, pre_seq):
        cur_num = 0
        seq_len = len(pre_seq)
        now_seq = ""
        i = 0
        while i < seq_len:
            tmp_num = pre_seq[i]
            while i < seq_len and tmp_num == pre_seq[i]:
                i += 1
                cur_num += 1
            now_seq += str(cur_num) + tmp_num
            cur_num = 0
        return now_seq



s = Solution()
#pre_seq = "21"
#print s.countAndSayNext(pre_seq)
print s.countAndSay(2)