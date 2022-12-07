class Solution:
    def isIsomorphic(self, s: str, t: str):
        s_dic = {}
        t_dic = {}
        i = 0
        s_li = []
        t_li = []
        for k in s:
            if k not in s_dic:
                s_dic[k] = i
                i += 1

        for word in s:
            s_li.append(s_dic[word])

        i = 0

        for k in t:
            if k not in t_dic:
                t_dic[k] = i
                i += 1

        for word in t:
            t_li.append(t_dic[word])

        if s_li == t_li:
            return True
        else:
            return False