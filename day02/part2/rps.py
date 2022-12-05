
class RockPaperScissors:

    # Order is rock, paper, scissors
    throws_opponent = [ "A", "B", "C" ]
    points_throw = [ 1, 2, 3 ] # Rock=1,Paper=2,Scissors=3
    game_outcome = {
        "X": 0, # Loss
        "Y": 3, # Draw
        "Z": 6  # Win
    }

    def __init__(self) -> None:
        self.total_score = 0

    def play(self, opponent: str, outcome: str) -> int:
        
        # Adds points for the required outcome
        round_score = self.game_outcome.get(outcome)

        # Add score for your throw
        # index N always loses to index N+1 as seen in part 1
        if outcome == "X":  # Loss
            offset = -1
        elif outcome == "Y":# Draw
            offset = 0
        else:               # Win
            offset = 1

        throw_opp = self.throws_opponent.index(opponent)
        round_score += self.points_throw[(throw_opp + offset) %3 ]

        self.total_score += round_score

    def score(self) -> int:
        return self.total_score