def f(x, y=[]):
    y.append(x)
    return y

print(f(1))

print(f(2, [3]))

print(f(3))