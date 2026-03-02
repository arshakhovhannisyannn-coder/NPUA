import numpy as np

# ↑ վերև սլաք
up_arrow = np.array([
[0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,1,1,0,0,0],
[0,0,0,1,1,1,1,1,0,0],
[0,0,1,1,0,1,0,1,1,0],
[0,1,1,0,0,1,0,0,1,1],
[0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0]
])

# ↓ ներքև սլաք
down_arrow = np.array([
[0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,1,0,0,0,0],
[0,1,1,0,0,1,0,0,1,1],
[0,0,1,1,0,1,0,1,1,0],
[0,0,0,1,1,1,1,1,0,0],
[0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0]
])

# ← ձախ սլաք
left_arrow = np.array([
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,1,0,0,0,0],
[0,0,0,1,1,1,0,0,0,0],
[0,0,1,1,0,1,0,0,0,0],
[1,1,1,1,1,1,1,0,0,0],
[0,0,1,1,0,1,0,0,0,0],
[0,0,0,1,1,1,0,0,0,0],
[0,0,0,0,1,1,0,0,0,0],
[0,0,0,0,0,1,0,0,0,0]
])

# → աջ սլաք
right_arrow = np.array([
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,1,1,0,0,0,0],
[0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,1,0,1,1,0,0],
[0,0,0,1,1,1,1,1,1,0],
[0,0,0,0,1,0,1,1,0,0],
[0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,1,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0,0]
])

# ====== Hopfield training ======
arrows = np.array([up_arrow, down_arrow, left_arrow, right_arrow])
patterns = np.array([np.where(a.reshape(-1) == 1, 1, -1) for a in arrows])

n = len(arrows)
m = len(patterns[0])

x = patterns[0].reshape(-1, 1)
W = x @ x.T / m

for i in range(1, n):
    x = patterns[i].reshape(-1, 1)
    W += x @ x.T / m

for i in range(m):
    W[i][i] = 0

# ====== Input (կարաս փոխես՝ up_arrow, down_arrow, noisy և այլն) ======
inp = np.copy(right_arrow)

# օրինակ՝ մի քիչ աղմուկ ավելացնենք
inp[5,3] = 0
inp[5,4] = 1
inp[2,5] = 0

s0 = np.where(inp.reshape(-1) == 1, 1, -1)

# ====== Iterative update ======
for iter in range(1000):
    sn = np.copy(s0)
    for i in range(m):
        h = 0
        for j in range(m):
            h += W[i][j] * s0[j]
        s0[i] = 1 if h >= 0 else -1
    if (sn == s0).all():
        print("lavaguyn iteraci ::", iter)
        break

# ====== Որ սլաքին է նման ======
similarities = [np.dot(s0, p) for p in patterns]
k = np.argmax(similarities)
labels = ["UP", "DOWN", "LEFT", "RIGHT"]
print("gushakac slaky ::", labels[k])
