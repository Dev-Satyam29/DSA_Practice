class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        width=max(0,min(rec2[2],rec1[2])-max(rec2[0],rec1[0]))
        height=max(0,min(rec2[3],rec1[3])-max(rec2[1],rec1[1]))
        area=width*height
        if area>0:
            return True
        else:
            return False
        