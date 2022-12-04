from elf import Elf

class Expedition:

    def __init__(self) -> None:
        self.elves = list()
        self.calories_max = 0

    def add(self, elf: Elf):
        self.elves.append(elf)
        self._adjust_max_calories(elf)
        
    def _adjust_max_calories(self, elf):
        if elf.calories() > self.calories_max:
            self.calories_max = elf.calories()