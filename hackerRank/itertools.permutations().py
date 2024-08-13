from itertools import permutations
S, k = input().split()
for i in sorted(permutations(S, int(k))):
    print("".join(i))


# Output:
# hack 2
# permutations(S, int(k)) generates: ('h', 'a'), ('h', 'c'), ('h', 'k'), ('a', 'h'), ('a', 'c'), ('a', 'k'), ('c', 'h'), ('c', 'a'), ('c', 'k'), ('k', 'h'), ('k', 'a'), ('k', 'c')
# Sort Permutations: ('a', 'c'), ('a', 'h'), ('a', 'k'), ('c', 'a'), ('c', 'h'), ('c', 'k'), ('h', 'a'), ('h', 'c'), ('h', 'k'), ('k', 'a'), ('k', 'c'), ('k', 'h')
# ac
# ah
# ak
# ca
# ch
# ck
# ha
# hc
# hk
# ka
# kc
# kh
