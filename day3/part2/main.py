from rucksack import Rucksack, overlap, priority

sum_prio = 0

with open("../input.txt", "r") as file:

    group = list()

    for line in file:
        line = line.strip()
        group.append(Rucksack(line))
        
        # Every 3rd rucksack, check overlap and save prio
        if len(group) == 3:
            group_overlap = overlap(group)
            sum_prio += priority(group_overlap)
            group = list()
print(sum_prio)