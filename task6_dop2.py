import numpy as np
import matplotlib.pyplot as plt

def plot_ellipse(epsilon, p):
    # Проверка на допустимость эксцентриситета
    if not (0 <= epsilon < 1):
        raise ValueError("Экстремаситет должен быть в диапазоне [0, 1)")

    # Углы φ от 0 до 2π
    phi = np.linspace(0, 2 * np.pi, 1000)

    # Рассчитываем радиус r по формуле
    r = p / (1 + epsilon * np.cos(phi))

    # Преобразуем полярные координаты в декартовы
    x = r * np.cos(phi)
    y = r * np.sin(phi)

    # Создаем график
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label=f'Эллипс: ε={epsilon}, p={p}')
    plt.title('График эллипса в полярной системе координат')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axis('equal')  # Равные единицы по обеим осям
    plt.grid()
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.legend()
    plt.show()
    plt.savefig('fig_10.png')

# Пример использования функции
plot_ellipse(epsilon=0.5, p=2)