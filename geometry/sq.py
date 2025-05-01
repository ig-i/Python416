class Square:
    def __init__(self, a):
        self.a = a

    def perimeter(self):
        return 4 * self.a


s1 = Square(10)
s2 = Square(20)
print(s1.perimeter())
print(s2.perimeter())
