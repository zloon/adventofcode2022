from elf import Elf
from expedition import Expedition

exp = Expedition()

with open("../input.txt", "r") as file:
    elf = Elf()
    
    for line in file:
        line=line.strip()
        
        if line == "":
            exp.add(elf)
            elf = Elf()
        else:
            elf.add_calories(int(line))

print(sum(exp.leaderboard()))