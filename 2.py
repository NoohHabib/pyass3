from itertools import product

A = list(map(int, input("enter").split()))
B = list(map(int, input("enter").split()))

cartesian_product = list(product(A, B))

for pair in cartesian_product:
    print(pair, end=" ")