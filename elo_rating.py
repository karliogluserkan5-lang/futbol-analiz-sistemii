import math

class EloRating:
    def __init__(self, k_factor=32):
        self.k = k_factor
    
    def expected_score(self, rating_a, rating_b):
        return 1 / (1 + math.pow(10, (rating_b - rating_a) / 400))
    
    def update_rating(self, rating_a, rating_b, score_a, score_b):
        expected_a = self.expected_score(rating_a, rating_b)
        expected_b = self.expected_score(rating_b, rating_a)
        
        new_rating_a = rating_a + self.k * (score_a - expected_a)
        new_rating_b = rating_b + self.k * (score_b - expected_b)
        
        return round(new_rating_a, 2), round(new_rating_b, 2)

if __name__ == "__main__":
    elo = EloRating()
    print(elo.expected_score(1500, 1400))
    print(elo.update_rating(1500, 1400, 1, 0))
