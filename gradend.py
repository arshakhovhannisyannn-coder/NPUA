import numpy as np
import matplotlib.pyplot as plt   # ← Ահա գրադարանը

def f_prime(x):
    return 2*(x + 2)

def f(x):
    return (x + 2)**2 + 5

x = 10          # start point
lr = 0.1       # learning rate
eps = 0.0001    # precision
xs = []        # պահպանելու ենք x-ի արժեքները քայլ առ քայլ
ys = []        # համապատասխան f(x)-երը
i = 0
while True:
    
    if x - (x-lr * f_prime(x)) <= eps:
        break
    xs.append(x)
    ys.append(f(x))
    x = x - lr * f_prime(x)
    i+=1
    print(i, x)

# ---- Գծապատկեր ----
plt.plot(xs, ys, marker='o')
plt.xlabel("x value")
plt.ylabel("f(x) value")
plt.grid(True)
plt.show()
