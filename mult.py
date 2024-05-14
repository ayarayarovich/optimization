def f(x1, x2, r, lambd):
    return (
        3 * x1**2
        + x2**2
        - x1 * x2
        + x1
        + (r / 2) * (2 * x1 + x2 - 1) ** 2
        + lambd * (2 * x1 + x2 - 1)
    )


def grad1(x1, x2, r, lambd):
    return 6 * x1 - x2 + 1 + r * (2 * x1 + x2 - 1) + lambd * (2 * x1 + x2 - 1)


def grad2(x1, x2, r, lambd):
    return 2 * x2 - x1 + r * (2 * x1 + x2 - 1) + lambd


def sys2(r, lambd):
    return (3 * r + 1 - lambd) / (15 + 8 * r)


def sys1(r, lambd):
    return 7 * (sys2(r, lambd)) - 1


def lambdaf(r, lambd):
    return lambd + r * (sys2(r, lambd) + sys1(r, lambd) - 1)


x = [0, 0]
gf = [0, 0]
file1 = open("data.txt", mode="r")
file2 = open("answer.txt", mode="w")
n = int(file1.readline())
file2.write(f"n = {n}\n")
r = [float(i) for i in file1.readline().split()]
file2.writelines(f"r = {ri} " for ri in r)
lambd = int(file1.readline())
file2.write(f"lambda = {lambd}\n")
epsilon = float(file1.readline())
file2.write(f"epsilon = {epsilon}\n")
k = 0
x[0] = sys1(r[k], lambd)
x[1] = sys2(r[k], lambd)
file2.write(f"x{k} = [{x[0]}, {x[1]}]\n")
file2.write(
    f"P(x{k},lambd{k},r{k}) = {(r[k] / 2)*(((2*x[0] + x[1]) - 1) ** 2) + lambd * (2*x[0] + x[1] - 1)}\n"
)
file2.write(f"Функция: 3x1^2 + x2^2 - x1*x2 + x1\n")
while (r[k] / 2) * (((2 * x[0] + x[1]) - 1) ** 2) + lambd * (
    2 * x[0] + x[1] - 1
) >= epsilon:
    lambd = lambdaf(r[k], lambd)
    file2.write(f"k = {k}\n")
    H = [[0, 0], [0, 0]]
    H[0][0] = 2 + r[k]
    H[0][1] = H[1][0] = 1 + r[k]
    H[1][1] = 8 + r[k]
    det = H[0][0] * H[1][1] - H[1][0] * H[0][1]
    file2.write(f"H = {H[0][0]}, {H[0][1]}, \n    {H[1][0]}, {H[1][1]}\n")
    if det > 0:
        file2.write(f"Выполняется достаточное условие\n")
    flag = 0
    file2.write(f"r{k} = {r[k]}\n")
    file2.write(f"lambda{k} = {lambd}\n")
    x[0] = sys1(r[k], lambd)
    x[1] = sys2(r[k], lambd)
    file2.write(f"x{k} = [{x[0]}, {x[1]}]\n")
    k += 1
file2.write(f"Точка минимума x* = ({x[0]}, {x[1]})\n")
file2.write(f"Значение функции в точке минимума f(x*) = {f(x[0], x[1], r[k], lambd)}\n")
