class ZeroProduct(Exception):
    def __init__(self, message=None):           # type: ignore[no-untyped-def]
        super().__init__(message)
