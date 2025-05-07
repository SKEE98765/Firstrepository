class Shape:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def calculateArea(self):
        # Base class doesn't define area - this should be overridden
        raise NotImplementedError("Subclasses must implement calculateArea()")

    def displayDetails(self):
        print(f"Side 1: {self.side1}")
        print(f"Side 2: {self.side2}")
        print(f"Area: {self.calculateArea()}")


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)

    def calculateArea(self):
        return self.side1 * self.side2

    def displayDetails(self):
        print("Shape: Rectangle")
        super().displayDetails()


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(base, height)

    def calculateArea(self):
        return 0.5 * self.side1 * self.side2

    def displayDetails(self):
        print("Shape: Triangle")
        super().displayDetails()


# Test cases
def test_shapes():
    print("=== Rectangle Test ===")
    r1 = Rectangle(10, 5)
    r1.displayDetails()

    print("\n=== Triangle Test ===")
    t1 = Triangle(8, 6)
    t1.displayDetails()

    print("\n=== Another Rectangle ===")
    r2 = Rectangle(3.5, 4.5)
    r2.displayDetails()

    print("\n=== Another Triangle ===")
    t2 = Triangle(7, 10)
    t2.displayDetails()


# Run tests
if __name__ == "__main__":
    test_shapes()
