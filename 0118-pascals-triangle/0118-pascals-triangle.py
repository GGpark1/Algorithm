class Solution:
    def generate(self, numRows):
        tri_list = []
        for i in range(1, numRows+1):
            tri_list = tri_list + ([[1] * i])

        for i, row in enumerate(tri_list[1:-1], start=2):
            for j in range(len(row)-1):
                new_num = row[j] + row[j+1]
                tri_list[i][j+1] = new_num
        return tri_list
