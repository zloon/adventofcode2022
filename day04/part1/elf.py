
class Elf:

    def __init__(self, assignment_range: str) -> None:
        self.assignment_limits = assignment_range.split("-")
        self.assignment_min = int(self.assignment_limits[0])
        self.assignment_max = int(self.assignment_limits[1])
        self.assignment_size = self.assignment_max - self.assignment_min

def fully_overlapping(elf_one: Elf, elf_two: Elf) -> bool:
    # identify the shortest range
    if elf_one.assignment_size < elf_two.assignment_size :
        shortest_range = elf_one
        longest_range = elf_two
    else: 
        shortest_range = elf_two
        longest_range = elf_one

    # Check if the shortest range is within the longest range
    if (shortest_range.assignment_min >= longest_range.assignment_min and
        shortest_range.assignment_max <= longest_range.assignment_max):
        return True
    
    return False