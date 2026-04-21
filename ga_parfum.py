import random
import math

MIN = -10
MAX = 10
POP_SIZE = 50
GENERATIONS = 100

# fungsi dari soal
def fitness_function(x1, x2):
    f = -(math.sin(x1) * math.cos(x2) * math.tan(x1 + x2)
          + 0.5 * math.exp(1 - abs(x1)))
    return 1 / (1 + f)

# individu
def create_individual():
    return {
        "x1": random.uniform(MIN, MAX),
        "x2": random.uniform(MIN, MAX)
    }

# hitung fitness
def evaluate(ind):
    ind["fitness"] = fitness_function(ind["x1"], ind["x2"])

# inisialisasi populasi
def init_population():
    pop = []
    for _ in range(POP_SIZE): #loop sebanyak popsize
        ind = create_individual() #gEnerate individu
        evaluate(ind) #hitung fitness
        pop.append(ind) #simpen ke populasi
    return pop

# selection (tournament)
def select(pop):
    best = random.choice(pop) #ambil individu random sebagai kandidat awal
    for _ in range(2):
        challenger = random.choice(pop) #individu penantang
        if challenger["fitness"] > best["fitness"]:
            best = challenger #milih fitness terbesar
    return best

# crossover
def crossover(p1, p2):
    alpha = random.random() #0 1 untuk kombinasi
    return {
        "x1": alpha * p1["x1"] + (1 - alpha) * p2["x1"],
        "x2": alpha * p1["x2"] + (1 - alpha) * p2["x2"] #campuran dari kedua parent
    }

# mutasi
def mutate(ind):
    if random.random() < 0.1: #probabilitas mutasi 10%
        ind["x1"] += random.uniform(-1, 1)
        ind["x2"] += random.uniform(-1, 1)

    # batas domain
    ind["x1"] = max(MIN, min(MAX, ind["x1"]))
    ind["x2"] = max(MIN, min(MAX, ind["x2"]))

# main
population = init_population()

for gen in range(GENERATIONS):
    new_pop = []

    for _ in range(POP_SIZE):
        p1 = select(population)
        p2 = select(population)

        child = crossover(p1, p2)
        mutate(child)
        evaluate(child)

        new_pop.append(child)

    population = new_pop

# cari terbaik
best = max(population, key=lambda x: x["fitness"])

# hitung nilai fungsi asli
f_value = -(math.sin(best["x1"]) * math.cos(best["x2"]) * math.tan(best["x1"] + best["x2"])
            + 0.5 * math.exp(1 - abs(best["x1"])))

print("=== HASIL TERBAIK ===")
print("x1 =", best["x1"])
print("x2 =", best["x2"])
print("fitness =", best["fitness"])
print("f(x1,x2) =", f_value)