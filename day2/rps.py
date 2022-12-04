
class RockPaperScissors:

    # Order is rock, paper, scissors
    throws = [ "A", "B", "C", "X", "Y", "Z"]

    points = {
        "win": 6,
        "draw": 3,
        "loss": 0,
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    def __init__(self) -> None:
        self.total_score = 0

    def play(self, opponent: str, you: str) -> int:

        # Add score for your chosen throw
        round_score = self.points[you]

        # Add score for outcome
        if self.throws.index(you)%3 > self.throws.index(opponent)%3: # win
            round_score += self.points['win']
        elif self.throws.index(you)%3 == self.throws.index(opponent)%3: # draw
            round_score += self.points['draw']

        self.total_score += round_score

    def score(self) -> int:
        return self.total_score