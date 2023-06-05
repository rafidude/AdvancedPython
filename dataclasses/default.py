from dataclasses import dataclass


@dataclass
class Point:
    x: int = 0
    y: int = 0


p = Point()
print(p)

p2 = Point(1, 2)
print(p2)
