
class Elf:

    def __init__(self, assignment_range: str) -> None:
        self.assignment_limits = assignment_range.split("-")
        self.assignment_min = int(self.assignment_limits[0])
        self.assignment_max = int(self.assignment_limits[1])
        self.assignment_size = self.assignment_max - self.assignment_min

def partially_overlapping(elf_one: Elf, elf_two: Elf) -> bool:

    if (elf_one.assignment_min <= elf_two.assignment_max and
        elf_one.assignment_max >= elf_two.assignment_min or
        
        elf_two.assignment_min <= elf_one.assignment_max and
        elf_two.assignment_max >= elf_one.assignment_min):
        return True
    
    return False