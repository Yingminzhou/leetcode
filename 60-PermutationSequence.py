class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        n_seq = 1
        for i in range(1, n):
            n_seq *= i
        start_num = (k-1) / n_seq + 1
        new_k = k - (start_num - 1) * n_seq
        idx = 1
        seq_list = list()
        for i in range(1, n+1):
            if i != start_num:
                seq_list.append(i)
        while idx < new_k:
            seq_list = self.getNextPermutation(seq_list)
            idx += 1
        ans = ""
        if start_num > 0:
            ans += str(start_num)
        for i in seq_list:
            ans += str(i)
        return ans


    def getNextPermutation(self, seq_list):
        for i in range(len(seq_list)-1, -1, -1):
            if i >= 1 and seq_list[i] < seq_list[i-1]:
                continue
            seq_list = seq_list[:i-1] + self.insertVal(seq_list[i-1:])
            return seq_list
        return seq_list

    def insertVal(self, sub_list):
        if len(sub_list) <= 1:
            return sub_list
        pivot = sub_list[0]
        for i in range(len(sub_list)-1, 0, -1):
            if pivot > sub_list[i]:
                continue
            else:
                sub_list[0], sub_list[i] = sub_list[i], sub_list[0]
                break
        interval = (len(sub_list) - 1)/2
        for i in range(1, interval+1):
            sub_list[i], sub_list[len(sub_list)-i] =  sub_list[len(sub_list)-i], sub_list[i]
        return sub_list




s = Solution()
ans = s.getPermutation(3,5)
print ans