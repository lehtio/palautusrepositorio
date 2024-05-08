class TennisGame:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.scores = {player1_name: 0, player2_name: 0}

    def won_point(self, player_name):
        if player_name in self.scores:
            self.scores[player_name] += 1

    def get_score(self):
        p1_score = self.scores[self.player1_name]
        p2_score = self.scores[self.player2_name]

        if p1_score == p2_score:
            return self._even_score(p1_score)
        if self._is_advantage_or_win(p1_score, p2_score):
            return self._advantage_or_win(p1_score, p2_score)
        return self._standard_score(p1_score, p2_score)

    def _even_score(self, score):
        return f"{self.SCORE_NAMES[score]}-All" if score < 3 else "Deuce"

    def _is_advantage_or_win(self, score1, score2):
        return max(score1, score2) >= 4

    def _advantage_or_win(self, score1, score2):
        diff = score1 - score2
        if abs(diff) == 1:
            return f"Advantage {self._leading_player(score1, score2)}"
        return f"Win for {self._leading_player(score1, score2)}"

    def _leading_player(self, score1, score2):
        return self.player1_name if score1 > score2 else self.player2_name

    def _standard_score(self, score1, score2):
        return f"{self.SCORE_NAMES[score1]}-{self.SCORE_NAMES[score2]}"
