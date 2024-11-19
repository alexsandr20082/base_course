import random
flowers = ["Роза", "Тюльпан", "Лилия"]
colors = ["Красный", "Синий", "Желтый", "Зеленый", "Белый"]

flower_colors = {flower: random.choice(colors) for flower in flowers}

print(f"Словарь цветков и цветов: {flower_colors}")