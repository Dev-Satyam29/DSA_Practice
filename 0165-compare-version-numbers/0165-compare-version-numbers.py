class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n = len(v1)
        m = len(v2)
        i = 0
        j = 0
        while i < n or j < m:
            if i < n:
                num1 = int(v1[i])
            else:
                num1 = 0
            if j < m:
                num2 = int(v2[j])
            else:
                num2 = 0
            if num1 < num2:
                return -1
            if num1 > num2:
                return 1
            i += 1
            j += 1
        return 0