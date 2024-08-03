class A:
    def __init__(self):
        self.number = 1
        
class B(A):
    def __init__(self):
        self.number = 2

class C(A):
    def __init__(self):
        self.number = 3

class D(A):
    def __init__(self):
        self.number = 4

class E(B, C):
    def __init__(self):
        self.number = 5

class F(C, D):
    def __init__(self):
        self.number = 6

class G(E, F):
    def __init__(self):
        self.number = 7


g = G()
print(g.number)