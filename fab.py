a, b = 0, 1
num_terms = 10
for _ in range(num_terms):
    print(a, end=" ")
    a, b = b, a + b
