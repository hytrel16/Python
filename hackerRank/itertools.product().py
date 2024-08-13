from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*list(product(A, B)))    


# Output:
# 1 2 3
# 4 5
# (1, 4) (1, 5) (2, 4) (2, 5) (3, 4) (3, 5)
