class Cake:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
x,y,z = map(int, input().split())
A = Cake(x,y,z)
x,y,z = map(int, input().split())
C = Cake(x,y,z)

print(
    int(C.x - A.z),
    int(C.y / A.y),
    int(C.z - A.x),
)