class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cl = 0
        cr = 0
        cu = 0
        cd = 0
        for i in moves:
            if i=="U":
                cu+=1
            elif i=="D":
                cd+=1
            elif i=="L":
                cl+=1
            else:
                cr+=1
        if abs(cl-cr)==0 and abs(cu-cd)==0:
            return True
        else:
            return False
        