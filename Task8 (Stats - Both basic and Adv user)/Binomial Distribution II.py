# Enter your code here. Read input from STDIN. Print output to STDOUT
def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return factorial(n - 1) * n

def binomial(x, n, p):
    f = factorial(n) / (factorial(n - x) * factorial(x))
    return (f * p**x * (1.0 - p)**(n-x))

values = list(map(float, input().split()))
p = (values[0] / 100)
n = int(values[1])


no_more_than_2_rejects = 0
for i in range(n):
    if i < 3:
        no_more_than_2_rejects = no_more_than_2_rejects + binomial(i, n, p)
print(round(no_more_than_2_rejects, 3))


at_least_2_rejects = 0
for i in range(n):
    if i > 1:
        at_least_2_rejects = at_least_2_rejects + binomial(i, n, p)
print(round(at_least_2_rejects, 3))
