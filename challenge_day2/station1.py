# observation1 = [50, 12586269025, 45, 1134903170]
# observation2 = [52, 32951280099, 35, 9227465]
# observation3 = [84, 160500643816367100, 27, 196418]


def solution_staion_1():
    n=int(input())

a, b = 0, 1

for i in range(n):
    a, b = b, a + b
print(a)