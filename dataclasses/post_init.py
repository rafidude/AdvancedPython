from dataclasses import dataclass


@dataclass
class Circle:
    radius: float

    def __post_init__(self):
        self.area = 3.14 * (self.radius**2)


c = Circle(2)
print(c.area)
