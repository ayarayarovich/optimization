from math import sqrt

def f(x1, x2):
    return 3 * x1 ** 2 + x2 ** 2 - x1 * x2 + x1

H_rev = [[4 / 27, -2 / 27], [-2 / 27, 2 / 27]]
M = 50
eps1, eps2 = 0.1, 0.15
x0 = [1, 2]

def f_vec(x):
    return f(x[0], x[1])

def gradient(f, x1, x2):
    h = 1e-6
    return [(f(x1 + h, x2) - f(x1 - h, x2)) / (2 * h), (f(x1, x2 + h) - f(x1, x2 - h)) / (2 * h)]

def gradient_vec(f, x):
    return gradient(f, x[0], x[1])

def norm(x1, x2):
    return sqrt(x1 ** 2 + x2 ** 2)

def norm_vec(x):
    return sqrt(x[0] ** 2 + x[1] ** 2)

def mat_x_vec(mat, vec):
    result = []
    for i in range(len(mat)):
        result.append(0)
        for j in range(len(vec)):
            result[i] += mat[i][j] * vec[j]
    return result

def golden_ratio(f, a0, b0, l):
    a, b = a0, b0
    x = a0 + (3 - sqrt(5)) / 2 * (b0 - a0)
    y = a0 + b0 - x
    while abs(a - b) > 2 * l:
        if f(x) <= f(y):
            b = y
            y = x
            x = a + b - x
        else:
            a = x
            x = y
            y = a + b - y
    return (a + b) / 2

x = []
x.append(x0)
k = 0
first_check = False
while k < M:
    d_k = [-x for x in mat_x_vec(H_rev, gradient_vec(f, x[-1]))]

    def fi(t):
        return f_vec([x[-1][i] + t * d_k[i] for i in range(2)])

    a, b = -10, 10
    t_min = a
    while t_min == a or t_min == b:
        t_min = golden_ratio(fi, a, b, eps1)
        if abs(t_min - a) <= eps1:
            a -= 1
            b -= 10
            t_min = a
        if abs(t_min - b) <= eps1:
            a += 10
            b += 10
            t_min = a

    x.append([x[-1][i] + d_k[i] * t_min for i in range(2)])

    if norm_vec(gradient_vec(f, x[-1])) < eps1:
        break
    if k > 1 and norm_vec([x[-1][i] - x[-2][i] for i in range(2)]) < eps2:
        if first_check:
            break
        else:
            first_check = True
    else:
        first_check = False
    k += 1

print("x =", x[-1])
print("f(x) =", f_vec(x[-1]))