import numpy as np
from scipy.stats import poisson

def skor_olasiligi(home_xg, away_xg, max_goal=5):
    prob_matrix = np.zeros((max_goal+1, max_goal+1))
    for i in range(max_goal+1):
        for j in range(max_goal+1):
            prob_matrix[i][j] = poisson.pmf(i, home_xg) * poisson.pmf(j, away_xg)
    
    home_win = np.sum(np.tril(prob_matrix, -1))
    draw = np.sum(np.diag(prob_matrix))
    away_win = np.sum(np.triu(prob_matrix, 1))
    
    return {
        "home_win": round(home_win * 100, 2),
        "draw": round(draw * 100, 2),
        "away_win": round(away_win * 100, 2),
        "score_matrix": prob_matrix
    }

if __name__ == "__main__":
    print(skor_olasiligi(1.5, 1.2))
