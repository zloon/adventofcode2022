class Stack:

    def __init__(self, stack_id: int) -> None:
        self.stack_id = stack_id
        self.crates = ""

    def top(self) -> str:
        return self.crates[-1] if len(self.crates) > 0 else ""

    def add_crate(self, crate_id: str):
        self.crates += str(crate_id)

    def remove_crate(self) -> str:
        removed_crate = self.top()
        if self.top() != "":
            self.crates = self.crates[:-1]

        return removed_crate

    
class Crane:

    def __init__(self, description: list) -> None:
        description.reverse()

        # first item is the different stacks
        self.stacks = self._get_stacks(description[0])
        # remaining items describes the crates
        self._populate_stacks(self.stacks, description[1:])

    def move(self, instruction: str):
        instruction_list = instruction.split(" ")

        count = int(instruction_list[1])
        source = int(instruction_list[3]) - 1       # list index is 1 less than instruction
        destination = int(instruction_list[5]) - 1  # list index is 1 less than instruction

        moved_crates = ""
        for move in range(1, count + 1):
            moved_crates += self.stacks[source].remove_crate()
        
        for crate in moved_crates[::-1]:
            self.stacks[destination].add_crate(crate)


    def _get_stacks(self, line: str) -> list:
        stacks = list()
        stack_ids = line.strip().split(" ")

        for stack_id in stack_ids:
            if stack_id != "":
                stacks.append(Stack(stack_id))

        return stacks

    def _populate_stacks(self, stacks: list, description: list):
        # Count the number of crates depending on row width, each crate
        # takes up 3 chars, plus 1 space after each excetp the last
        # row length = crates*4 - 1 -> row_length +1 / 4 = crates
        num_crates = ( len(description[0]) + 1 ) // 4
        
        for line in description:
            for num in range(num_crates):
                # crate id is the 2nd char of each crate,
                # e.g. char 2, 6, 10, ... of each row
                crate_id_pos = num * 4 + 1
                
                # If there is a crate (non-emtpy ID), add it to the stack
                if len(line) > crate_id_pos and line[crate_id_pos] != " ":
                    stacks[num].add_crate(line[crate_id_pos])