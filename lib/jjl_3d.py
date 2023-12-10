
# Creating a Point class for coordinates
# class Point():
#     def __init__(self, x=None, y=None, z=None, data=None) -> None:
#         self.x = x
#         self.y = y
#         self.z = z
#         self.data = data 
#     def add(self, apoint) -> None:
#         self.x += apoint.x
#         self.y += apoint.y
#         self.z += apoint.z
#     def mult(self, apoint) -> None:
#         self.x *= apoint.x
#         self.y *= apoint.y
#         self.z *= apoint.z
#     def print(self) -> None:
#         print(f"{self.x}, {self.y}, {self.z}")

class Point2D():
    def __init__(self, x=None, y=None, data=None) -> None:
        self.x = x
        self.y = y
        self.data = data 
    def add(self, apoint) -> None:
        self.x += apoint.x
        self.y += apoint.y
    def mult(self, apoint) -> None:
        self.x *= apoint.x
        self.y *= apoint.y
    def print(self) -> None:
        print(f"{self.x}, {self.y}")


class Point3D(Point2D): 
    def __init__(self, x, y, z, data) -> None:
        super().__init__(x=x, y=y, data=data)
        self.z =  z

    def add(self, apoint) -> None:
        super().add(apoint)
        self.z += apoint.z
    
    def mult(self, apoint) -> None:
        super().mult(apoint)
        self.z *= apoint.z
    
    def print(self) -> None:
        print(f"{self.x}, {self.y}, {self.z}")

