class SppData:
    def __init__(self, data: str):
        self.raw_data = data

    def as_hex(self) -> str:
        return self.raw_data.upper().replace(":", "")

    def __str__(self):
        return self.as_hex()
