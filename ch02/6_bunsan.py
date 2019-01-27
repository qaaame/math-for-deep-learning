import math

def var(data):
    ave = sum(data) / len(data)
    total = 0
    for i in data:
        total += (ave -i) ** 2
        return total / len(data)

def std(data):
    return math.sqrt(var(data))

a = [72,61,91,31,45]

# print(sum(a)/len(a))

print(var(a))

print(std(a))