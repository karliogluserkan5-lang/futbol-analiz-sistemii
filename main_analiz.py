import numpy as np
from poisson_model import skor_olasiligi
from elo_rating import EloRating
from xg_model import hesapla_xg
from edge_calculator import edge_hesapla
from form_analysis import form_puani, trend_analizi
from monte_carlo import monte_carlo_simulasyon, skor_dagilimi

def analiz_et(home_xg, away_xg, home_elo, away_elo, home_form, away_form, home_odds, draw_odds, away_odds):
    poisson = skor_olasiligi(home_xg, away_xg)
    elo = EloRating()
    home_exp = round(elo.expected_score(home_elo, away_elo) * 100, 1)
    
    home_edge = edge_hesapla(home_odds, poisson['home_win'])
    draw_edge = edge_hesapla(draw_odds, poisson['draw'])
    away_edge = edge_hesapla(away_odds, poisson['away_win'])
    
    print(f"Poisson: Ev %{poisson['home_win']} Ber %{poisson['draw']} Dep %{poisson['away_win']}")
    print(f"Elo: Ev kazanma ihtimali %{home_exp}")
    print(f"Monte Carlo: {monte_carlo_simulasyon(home_xg, away_xg)}")
    print(f"En olası 3 skor: {list(skor_dagilimi(home_xg, away_xg).items())[:3]}")
    print(f"Edge: Ev %{home_edge} Ber %{draw_edge} Dep %{away_edge}")

if __name__ == "__main__":
    analiz_et(1.5, 1.2, 1500, 1450, 15, 12, 1.85, 3.40, 4.00)
