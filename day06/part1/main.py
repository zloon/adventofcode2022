from message import Signal

lines = open("../input.txt", "r")

for line in lines.readlines():
    
    signal = Signal(line)

    signal.find_marker()
    print(signal.marker_pos)