class ope() :

    """
    >>> op = ope()
    >>> op.addi(2,3)
    5
    >>> op.div(6,2)
    3
    """
    def addi(self, x, y, z=0):
        return int(x) + int(y) + z

    def div(self, x, y):

        if x > y :
            return x//y
        else :
            return y//x

    def souss(self, x, y):
        return x-y

    def noce(self):
        return 0

    def hey(self):
        return 777 
