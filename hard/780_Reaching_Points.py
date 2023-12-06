class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if (tx <= sx and ty <= sy) or (tx == 0 or ty == 0):
            if sx == tx:
                return sy == ty or sy%sx == ty
            if sy == ty:
                return sx == tx or sx%sy == tx
            return False
        if tx > ty:
            return self.reachingPoints(sx, sy, tx%ty, ty)
        if tx < ty:
            return self.reachingPoints(sx, sy, tx, ty%tx)
