import pygame

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Función para dibujar los elementos del arreglo
def draw_elements(screen, array, color_positions={}, width=800, height=600):
    screen.fill(BLACK)
    font = pygame.font.Font(None, 36)
    title = font.render("BubbleSort", True, WHITE)

    screen.blit(title, (65 - title.get_width() // 2, 10))
    num_elements = len(array)
    bar_width = width // num_elements
    for i, value in enumerate(array):
        color = WHITE
        if i in color_positions:
            color = color_positions[i]
        bar_height = (value / 100) * height
        pygame.draw.rect(screen, color, (i * bar_width, height - bar_height, bar_width, bar_height))
    pygame.display.flip()

# Bubble Sort con visualización
def bubble_sort_visual(array, screen, width=800, height=600):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            draw_elements(screen, array, {j: RED, j + 1: GREEN}, width, height)
            pygame.time.delay(100)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                draw_elements(screen, array, {j: GREEN, j + 1: RED}, width, height)
                pygame.time.delay(100)
    draw_elements(screen, array, width=width, height=height)

# Test básico
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Visualización Bubble Sort")
    
    array = [random.randint(1, 100) for _ in range(20)]  # Generar 20 números aleatorios
    bubble_sort_visual(array, screen)
    
    # Esperar a que el usuario cierre la ventana
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
