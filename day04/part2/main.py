from elf import Elf, partially_overlapping

overlap_count = 0

with open("../input.txt", "r") as file:

    for line in file:
        ranges = line.strip().split(",")

        elves = list()

        elf_one = Elf(ranges[0])
        elf_two = Elf(ranges[1])

        if partially_overlapping(elf_one, elf_two):
            overlap_count += 1

print(overlap_count)