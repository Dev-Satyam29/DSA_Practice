class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x=max(x1,min(xCenter,x2))
        y=max(y1,min(yCenter,y2))
        sq=x-xCenter
        sq2=y-yCenter
        sq_dis=(sq*sq)+(sq2*sq2)
        if sq_dis<=radius*radius:
            return True
        else:
            return False
        