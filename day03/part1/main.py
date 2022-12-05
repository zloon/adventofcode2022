from rucksack import Rucksack

sum_prio = 0

with open("../input.txt", "r") as file:
    
    for line in file:
        line = line.strip()
        
        rucksack = Rucksack(line)

        sum_prio += rucksack.priority(rucksack.overlapping())

print(sum_prio)