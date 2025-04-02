import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

num_steps = 10
step_height = 1
step_width = 2
move_right_speed = 0.027
bounce_factor = 0.7

#Ступеньки
x_steps = np.arange(num_steps) * step_width
y_steps = np.arange(num_steps) * step_height


ball_radius = 0.2
ball_x = step_width / 2 
ball_y = num_steps * step_height + ball_radius 
velocity_y = 0 
gravity = -0.01   

fig, ax = plt.subplots()
ax.set_xlim(-1, num_steps * step_width + 1)
ax.set_ylim(0, num_steps * step_height + 3)

#Лестница
for i in range(num_steps):
    step = plt.Rectangle((x_steps[i], y_steps[i]), step_width, step_height, color='brown')
    ax.add_artist(step)

#Мяч
ball = plt.Circle((ball_x, ball_y), ball_radius, color='red')
ax.add_artist(ball)


def update(frame):
    global ball_y, velocity_y, ball_x

    ball_x += move_right_speed

    
    velocity_y  += gravity 
    ball_y += velocity_y 

    #Столкновение
    current_step = int(ball_x // step_width) 
    if current_step < num_steps and ball_y - ball_radius <= y_steps[current_step]:
        ball_y = y_steps[current_step] + ball_radius 
        velocity_y = -velocity_y * bounce_factor  


    if current_step == num_steps - 1 and velocity_y < 0:
        velocity_y = 0 

   
    ball.set_center((ball_x, ball_y))
    return ball,


ani = animation.FuncAnimation(fig, update, frames=300, interval=20)

plt.title("Анимация мяча, прыгающего по лестницу")
plt.grid()
plt.gca().set_aspect('equal', adjustable='box') 
plt.show()
ani.save('animation_7.gif')