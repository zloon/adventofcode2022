
class Signal:

    def __init__(self, message: str) -> None:
        self.message = message
        self.buffer = self.Buffer()
        self.marker = None
        self.marker_pos = None

    def find_marker(self):

        for pos, digit in enumerate(self.message):
            self.buffer.add(digit)
            print(f'Adding {digit} to buffer: {self.buffer.content}')
            if self.buffer.is_unique and pos > 3:
                self.marker = self.buffer.content
                self.marker_pos = pos + 1 # pos is 1 lower than num proccessed chars
                break

    class Buffer:

        def __init__(self, length: int = 4) -> None:
            self.content = list()
            self.is_unique = False

            for number in range(0,length):
                self.content += [None]
        
        def add(self, digit):
            self.content.append(digit)
            self.content.pop(0)
            
            self.is_unique = ( len(self.content) == len(set(self.content)) )
        