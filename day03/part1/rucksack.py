class Rucksack:

    def __init__(self, content = "") -> None:
        # Split the content in two compartments
        first_half, second_half = content[:len(content)//2], content[len(content)//2:]

        self.compartment_one = self.Compartment(first_half)
        self.compartment_two = self.Compartment(second_half)

    def overlapping(self) -> str:
        return ''.join(set(self.compartment_one.content).intersection(self.compartment_two.content))

    def priority(self, item: chr) -> int:
        # lowercase prio is 1-26, ord('a') is 97, giving an offset of 96
        # uppercase prio is 27-52, ord('A') is 65, giving an offset of -38
        return ord(item) - (96 if item.islower() else 38)

    class Compartment:

        def __init__(self, content) -> None:
            self.content = content