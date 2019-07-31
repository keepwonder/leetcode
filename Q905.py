# -*- coding:utf-8 -*- 
# @Author: Jone Chiang
# @Date  : 2019/7/31 15:13
# @File  : Q905
"""
数组
905. Sort Array By Parity
"""


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # B = []
        # for d in A.copy():
        #     if d % 2 != 0:
        #         B.append(A.pop(A.index(d)))
        #
        # return A+B

        # B = A.copy()
        # for i in B:
        #     if i % 2 == 1:
        #         A.pop(A.index(i))
        #         A.append(i)
        #     print(A)
        #
        # return A

        # return [i for i in A if i % 2 == 0] + [i for i in A if i % 2 == 1]

        # B = []
        # for i in A.copy():
        #     if i % 2 == 1:
        #         A.remove(i)
        #         B.append(i)
        # return A + B

        start, end = 0, len(A)-1
        while start < end:
            m, n = A[start], A[end]
            if m % 2 == 1 and n % 2 == 0:
                A[start], A[end] = n, m
            elif m % 2 == 1:
                end -= 1
            elif n % 2 == 0:
                start += 1
            else:
                start += 1
                end -= 1
        return A


if __name__ == '__main__':
    data = [3, 1, 2, 4]
    S = Solution()
    print(S.sortArrayByParity(data))
