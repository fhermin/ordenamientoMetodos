import pygame
import random
import sys

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def draw_elements(array, color_positions={}):
    screen.fill(BLACK)
    num_elements = len(array)
    bar_width = width // num_elements
    for i, value in enumerate(array):
        color = WHITE
        if i in color_positions:
            color = color_positions[i]
        bar_height = (value / 100) * height
        pygame.draw.rect(screen, color, (i * bar_width, height - bar_height, bar_width, bar_height))
    pygame.display.flip()

def bubble_sort_visual(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            draw_elements(array, {j: RED, j+1: GREEN})
            pygame.time.delay(100)
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                draw_elements(array, {j: GREEN, j+1: RED})
                pygame.time.delay(100)
    draw_elements(array)

# Generar 20 elementos aleatorios entre 1 y 100
elements = [random.randint(1, 100) for _ in range(20)]

# Imprimir valores iniciales
print("Valores iniciales:", elements)

# Bucle principal
running = True
bubble_sort_visual(elements)

# Imprimir valores finales
print("Valores finales:", elements)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
