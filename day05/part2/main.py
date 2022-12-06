from crane import Crane, Stack
    
lines = open("../input.txt", "r")

# Read first section of the file - the initial state
crane_input = list()

while True:
    line = str(lines.readline())
    if line.strip() == "":
        break
    else:
        crane_input.append(line)

crane = Crane(crane_input)

# Read second part of the file
for instruction in lines:
    crane.move(instruction)

top_crates = ''
for stack in crane.stacks:
    top_crates += stack.top()

print(top_crates)