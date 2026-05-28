class Player:
    def __init__(self, score=10):
        self.score = score

    def decrease_score(self):
        self.score -= 1

    def get_score(self):
        return self.score