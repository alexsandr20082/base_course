import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def collision(x, vx, y, vy):

    #Ступенька
    stairs = [
     {'x_start': 4, 'x_end': 6, 'y_level': 3},
     {'x_start': 6, 'x_end': 8, 'y_level': 5},
     {'x_start': 8, 'x_end': 10, 'y_level': 7},
     {'x_start': 10, 'x_end': 12, 'y_level': 9},
     {'x_start': 12, 'x_end': 14, 'y_level': 11},
    ]
    
    if y < 0:
        return vx, -vy
    

    # Проверка столкновений со ступеньками
    for stair in stairs:
        if (stair['x_start'] <= x <= stair['x_end']) and \
           (0 <= y - stair['y_level'] < 0.2) and \
           (vy < 0):
            return vx, -vy * 1.0 # Отскок 
    

    return vx, vy 

def move_func(s, t):

    x, vx, y, vy = s
    dx_dt = vx
    dvx_dt = 0
    dy_dt = vy
    dvy_dt = -9.8
    return [dx_dt,dvx_dt,dy_dt,dvy_dt]

def calc(x0, vx0, y0, vy0, T, N):

    x = [x0]
    y = [y0]

    tau = np.linspace(0, T, N)
    
    for k in range(N - 1):
        t_interval = [tau[k], tau[k+1]]
        s0 = (x0, vx0, y0, vy0)
        
        sol = odeint(move_func, s0, t_interval)
        
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
    return ball,


if __name__ == '__main__':

    # Параметры мяча
    v = 15
    alpha = 80 * np.pi / 180
    x0, y0 = 0, 0
    vx0 = v * np.cos(alpha)
    vy0 = v * np.sin(alpha)


    # Параметры анимации
    T, N = 10, 500
    x, y = calc(x0, vx0, y0, vy0, T, N)


    # Настройка графики
    fig, ax = plt.subplots()
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 15)
    

    #Cтупенька
    stairs = [
     {'x_start': 4, 'x_end': 6, 'y_level': 3},
     {'x_start': 6, 'x_end': 8, 'y_level': 5},
     {'x_start': 8, 'x_end': 10, 'y_level': 7},
     {'x_start': 10, 'x_end': 12, 'y_level': 9},
     {'x_start': 12, 'x_end': 14, 'y_level': 11},
    ]
    for stair in stairs:
        ax.plot([stair['x_start'], stair['x_end']], 
                [stair['y_level'], stair['y_level']], 
                'k-', lw=3)
        
    for i in range(len(stairs)-1) :
        current = stairs[i]
        next_stairs = stairs[i+1]
        ax.plot([current["x_end"], next_stairs["x_start"]],
                [current["y_level"], next_stairs["y_level"]],
                'k-',lw=3)
        

    ball, = ax.plot([], [], 'o', color='r', markersize=10)
    ani = FuncAnimation(fig, animate, frames=N, interval=30, blit=True)
    ani.save('ball_stairs.gif', writer='pillow')
    plt.show()

