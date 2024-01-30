import random
import string

# generujemy łańcuch s
s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
N = len(s)

# generujemy wzorzec
p = "consectetur"
M = len(p)

PI = [0] * (M + 1)

# dla wzorca obliczamy tablicę PI [ ] 
PI[0] = b = -1
for i in range(1, M + 1):
    while b > -1 and p[b] != p[i - 1]:
        b = PI[b]
    b += 1
    PI[i] = b

# wypisujemy wzorzec
print(p)

# wypisujemy łańcuch s
print(s)

# poszukujemy pozycji wzorca w łańcuchu
pp = b = 0
for i in range(N):
    while b > -1 and p[b] != s[i]:
        b = PI[b]

    if b + 1 == M:
        while pp < i - b:
            print(" ", end="")
            pp += 1
        print("^", end="")
        pp += 1
        b = PI[b]

print()
