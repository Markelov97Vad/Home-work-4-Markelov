import math

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a, b, c = map(float, input().split())
print(a,b,c)
discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")
# 1 3-4
# 1-2 1
# 1 2 4





