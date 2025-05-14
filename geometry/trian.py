class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    print(__name__)
    __autor__ = "Пользователь"

    if __name__ == "__main__":
        print(f"Module {__name__} (autor: {__autor__})")