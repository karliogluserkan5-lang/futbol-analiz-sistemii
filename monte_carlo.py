import numpy as np

def monte_carlo_simulasyon(home_xg, away_xg, sim=10000):
    home_win = 0
    draw = 0
    for _ in range(sim):
        h = np.random.poisson(home_xg)
        a = np.random.poisson(away_xg)
        if h > a: home_win += 1
        elif h == a: draw += 1
    away_win = sim - home_win - draw
    return round(home_win/sim*100,1), round(draw/sim*100,1), round(away_win/sim*100,1)

def skor_dagilimi(home_xg, away_xg, sim=10000):
    skorlar = {}
    for _ in range(sim):
        h = np.random.poisson(home_xg)
        a = np.random.poisson(away_xg)
        skor = f"{h}-{a}"
        skorlar[skor] = skorlar.get(skor, 0) + 1
    return {k: round(v/sim*100,1) for k, v in sorted(skorlar.items(), key=lambda x: x[1], reverse=True)[:10]}
