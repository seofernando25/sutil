

# Should work more on this...
class Matrix44(object):

    def __init__(self, zeroed=False):
        self.dat = [[0 for _ in range(4)] for _ in range(4)]
        if not zeroed:
            for n in range(min(len(self.dat), len(self.dat[0]))):
                self.dat[n][n] = 1

    def get_row(self, index):
        return self.dat[index]

    def get_col(self, index):
        ret = []
        for i in range(len(self.dat)):
            ret.append( self.dat[i][index])
        return ret

    def __mul__(self, other) :
        result = Matrix44(zeroed=True)
        for x in range(4):
            for y in range(4):
                mult_group = list(zip(self.get_row(y), other.get_col(x)))
                for a, b in mult_group:
                    result.dat[y][x] += a*b
        return result
