class Rucksack:

    def __init__(self, content = "") -> None:
        self.content = content

        # Split the content in two compartments
        first_half, second_half = content[:len(content)//2], content[len(content)//2:]

        self.compartment_one = self.Compartment(first_half)
        self.compartment_two = self.Compartment(second_half)

    def overlapping(self) -> str:
        return ''.join(set(self.compartment_one.content).intersection(self.compartment_two.content))

    class Compartment:

        def __init__(self, content) -> None:
            self.content = content

def priority(item: chr) -> int:
    # lowercase prio is 1-26, ord('a') is 97, giving an offset of 96
    # uppercase prio is 27-52, ord('A') is 65, giving an offset of -38
    return ord(item) - (96 if item.islower() else 38)

def overlap(rucksacks: list()) -> str:
    overlapping_items = set(rucksacks[0].content)

    for rucksack in rucksacks[1:]: # for each other rucksack
        overlapping_items = overlapping_items.intersection(rucksack.content)

    return ''.join(overlapping_items) # Converts to string and returns
