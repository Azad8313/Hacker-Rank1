import math

def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

initial_values = list(map(float, input().split()))
mean = initial_values[0]
std = initial_values[1]
val_first_question = float(input())
val_sec_third_question = float(input())


print (round(100 - (cumulative(mean, std, val_first_question) * 100), 2))
print (round(100 - (cumulative(mean, std, val_sec_third_question) * 100), 2))
print (round(cumulative(mean, std, val_sec_third_question) * 100, 2))
