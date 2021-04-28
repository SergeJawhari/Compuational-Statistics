# Birthday Problem

P = 1.0

K = 50

for k in range(1, K-1):
    P = P*((365 - k + 1) / 365)
    print(k, 1 - P)