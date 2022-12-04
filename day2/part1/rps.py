
class RockPaperScissors:

    # Order is rock, paper, scissors
    throws_opponent = [ "A", "B", "C" ]
    throws_you = [ "X", "Y", "Z"]

    points = {
        "win": 6,
        "draw": 3,
        "loss": 0,
        "X": 1, # Rock
        "Y": 2, # Paper
        "Z": 3 # Scissors
    }

    def __init__(self) -> None:
        self.total_score = 0

    def play(self, opponent: str, you: str) -> int:
        # Convert throws to an int, R = 0, P = 1, S = 2
        throw_you = self.throws_you.index(you)
        throw_opp = self.throws_opponent.index(opponent)

        # Add score for your chosen throw
        round_score = self.points[you]

        # Add score for outcome
        if throw_you == (throw_opp+1)%3: # Win if your index is 1 higher than your opponent's mod 3, as R<P<S<R
            round_score += self.points['win']
        elif throw_you == throw_opp: # draw
            round_score += self.points['draw']

        self.total_score += round_score

    def score(self) -> int:
        return self.total_score