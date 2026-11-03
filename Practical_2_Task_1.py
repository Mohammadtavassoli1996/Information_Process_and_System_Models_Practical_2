# Практическая работа № 2 — Задание № 1 — Вариант № 1
def f(x, y):
 return x * y**2 - x**2 + 1
h = 0.1
n = 10
# Метод Эйлера
x = 4.0
y = 0.7
euler = [y]
for i in range(n):
 y_new = y + h * f(x, y)
 x = x + h
 y = y_new
 euler.append(y)
# Метод Эйлера–Коши
x = 4.0
y = 0.7
euler_cauchy = [y]
for i in range(n):
 slope1 = f(x, y)
 y_predict = y + h * slope1
 slope2 = f(x + h, y_predict)
 y_new = y + h / 2 * (slope1 + slope2)
 x = x + h
 y = y_new
 euler_cauchy.append(y)
# Метод Рунге–Кутты четвертого порядка
x = 4.0
y = 0.7
runge_kutta = [y]
for i in range(n):
 k1 = h * f(x, y)
 k2 = h * f(x + h / 2, y + k1 / 2)
 k3 = h * f(x + h / 2, y + k2 / 2)
 k4 = h * f(x + h, y + k3)
 y_new = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
 x = x + h
 y = y_new
 runge_kutta.append(y)
# Общая таблица результатов
print(' x     Эйлер     Эйлер-Коши  Рунге-Кутта')
for i in range(n + 1):
 x = 4.0 + i * h
 print(f'{x:.1f} {euler[i]: .8f} {euler_cauchy[i]: .8f} {runge_kutta[i]: .8f}')
