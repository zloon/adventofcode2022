class Elf:

    def __init__(self) -> None:
        self.cal = 0

    def add_calories(self, cal: int):
        self.cal += cal

    def calories(self) -> int:
        return self.cal