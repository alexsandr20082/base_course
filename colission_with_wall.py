import numpy as np
from numpy import absolute as nabs
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def collision(x, vx, y, vy):
    if y < 0:
        VX, VY = vx, -vy
    else:
        VX, VY = vx, vy

    return VX, VY


def move_func(s, t):
    x, vx, y, vy = s

    dx_dt = vx
    dvx_dt = 0
    dy_dt = vy
    dvy_dt = -9.8  

    return dx_dt, dvx_dt, dy_dt, dvy_dt


def calc(x0, vx0, y0, vy0, T, N):
    # Массивы для записи итоговых координат объектов
    x = [x0]
    y = [y0]

    tau = np.linspace(0, T, N)

    # Цикл для расчета столкновений
    for k in range(N - 1):
        t = [tau[k], tau[k + 1]]
        s0 = x0, vx0, y0, vy0

        sol = odeint(move_func, s0, t)

        x0 = sol[1, 0]
        y0 = sol[1, 2]
        x.append(x0)
        y.append(y0)

        vx0 = sol[1, 1]
        vy0 = sol[1, 3]
        res = collision(x0, vx0, y0, vy0)
        vx0 = res[0]
        vy0 = res[1]

    return x, y


def animate(i):
    ball.set_data([x[i]], [y[i]])


if __name__ == '__main__':
    v = 15
    alpha = 80 * np.pi / 180

    x0 = 0
    vx0 = v * np.cos(alpha)
    y0 = 0
    vy0 = v * np.sin(alpha)

    s0 = x0, vx0, y0, vy0

    # Разбиение общего времени моделирования на интервалы
    T = 10
    N = 500

    x, y = calc(x0, vx0, y0, vy0, T, N)

    # Графический вывод
    fig, ax = plt.subplots()

    ball, = plt.plot([], [], 'o', color='r')
    edge = 15
    ax.set_xlim(0, edge)
    ax.set_ylim(0, edge)

    ani = FuncAnimation(fig, animate, frames=N, interval=30)
    ani.save('collision.gif')