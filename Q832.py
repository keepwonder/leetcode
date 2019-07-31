# -*- coding:utf-8 -*- 
# @Author: Jone Chiang
# @Date  : 2019/7/31 11:02
# @File  : Q832

"""
数组
832. Flipping an Image

"""


class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # res = []
        # for i in A:
        #     res.append([j+1 if j == 0 else j-1 for j in i[::-1]])
        # return res

        # res = []
        # for i in A:
        #     res.append(list(map(lambda x: 0 if x == 1 else 1, i[::-1])))
        # return res

        # return [[1 ^ i for i in row[::-1]] for row in A]

        for i in range(len(A)):
            low, high = 0, len(A[i]) - 1
            while low <= high:
                if A[i][low] == A[i][high]:
                    A[i][low] = 1 - A[i][low]
                    A[i][high] = A[i][low]
                low += 1
                high -= 1
        return A


if __name__ == '__main__':
    data = [[1, 1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 0]]
    S = Solution()
    print(S.flipAndInvertImage(data))
