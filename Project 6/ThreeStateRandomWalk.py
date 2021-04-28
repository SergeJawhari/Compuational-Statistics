# Three state random walk
# Steady state

p = float(input("Enter The probability of a jump to the 'right'."))

J = int(input("Enter the number of jumps wanted."))

S = 1 # Start position
N = 2 # Reflecting boundary

import random

# ----------------------------------------------------------------------

History = []

# Accumulators 
zero = 0
one = 0
two = 0

# ----------------------------------------------------------------------

for k in range(J):

    r = random.uniform(0,1)

    if S == 0:
        S = 1
    elif S == N:
        S = N - 1
    elif (S < N) and (S > 0):
        if r < p:
            S = S + 1
        else:
            S = S - 1
    History.append(S)

# ----------------------------------------------------------------------

for i in History:
    if i == 0:
        zero += 1
    elif i == 1:
        one += 1
    else:
        two += 1

print("The probability of being in state '0' is ",\
    zero/J, "state '1' ", one/J, "state'2'", two/J,'.')