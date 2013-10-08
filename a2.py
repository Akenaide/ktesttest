class ope :
    def addi(self, x, y, z=0):
        return x+y+z

    def div(self, x, y):

        if x > y :
            return x//y
        else :
            return y//x

    def souss(self, x, y):
        return x-y

    def noce(self):
        return 0

    def nop(self):
        return "nop"