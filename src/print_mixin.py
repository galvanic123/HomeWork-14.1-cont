class PrintMixin:
    def __init__(self):              # type: ignore[no-untyped-def]
        print(repr(self))

    def __repr__(self):           # type: ignore[no-untyped-def]
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
