from scipy.stats import poisson

def poisson_skor(ev_xg, dep_xg, max_gol=5):
    skorlar = {}
    for i in range(max_gol + 1):
        for j in range(max_gol + 1):
            prob = poisson.pmf(i, ev_xg) * poisson.pmf(j, dep_xg)
            skorlar[f"{i}-{j}"] = round(prob * 100, 2)
    return skorlar

def en_olası_skorlar(skorlar, n=3):
    return sorted(skorlar.items(), key=lambda x: x[1], reverse=True)[:n]

if __name__ == "__main__":
    skorlar = poisson_skor(1.8, 1.2)
    print(f"En olası skor: {max(skorlar, key=skorlar.get)}")
