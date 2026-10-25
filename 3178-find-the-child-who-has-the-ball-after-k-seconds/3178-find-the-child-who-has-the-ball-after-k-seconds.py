class Solution(object):
    def numberOfChild(self, n, k):
        ele = k // (n - 1)
        mod = k % (n - 1)
        return n - 1 - mod if ele % 2 else mod