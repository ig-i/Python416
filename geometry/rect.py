class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def perimeter(self):
        return 2 * (self.w + self.h)

    print(__name__)  # __main__

    __autor__ = "Admin"

    if __name__ == "__main__":
        print(f"Module {__name__} (autor: {__autor__})")