class ope() :
    def addi(self, x, y, z=0):
        return int(x) + int(y) + z

    def div(self, x, y):
        x = int(x)
        y = int(y)
        if x > y :
            return x//y
        else :
            return y//x

    def souss(self, x, y):
        return int(x) - int(y)

    def mul(self, x, y):
        return int(x) * int(y)
        
    def noce(self):
        return 0
