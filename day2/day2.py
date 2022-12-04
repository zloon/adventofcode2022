from rps import RockPaperScissors

with open("input.txt", "r") as file:
    
    tournament = RockPaperScissors()

    for line in file:
        if line != "\n":
            throws = line.strip().split(" ")
            tournament.play(throws[0], throws[1])

print(tournament.score())