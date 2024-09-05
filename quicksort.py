import pygame

# Función para dibujar el array en la pantalla
def draw_array(screen, array, color_positions=None, clear_bg=True):
    if clear_bg:
        screen.fill((0, 0, 0))  # Fondo negro
    
    if color_positions is None:
        color_positions = {}
    
    bar_width = screen.get_width() // len(array)
    max_height = screen.get_height()

    for i, val in enumerate(array):
        color = color_positions.get(i, (255, 255, 255))  # Blanco por defecto
        bar_height = int(val / max(array) * max_height)
        pygame.draw.rect(screen, color, pygame.Rect(i * bar_width, max_height - bar_height, bar_width, bar_height))

    pygame.display.update()

# Función de Quick Sort con visualización
def quick_sort(array, screen, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        # Partición
        pivot_index = partition(array, screen, low, high)
        # Ordenar partes recursivamente
        quick_sort(array, screen, low, pivot_index - 1)
        quick_sort(array, screen, pivot_index + 1, high)

def partition(array, screen, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            draw_array(screen, array, {i: (0, 255, 0), j: (255, 0, 0)})  # Verde y Rojo para intercambio
            pygame.time.delay(50)

    array[i + 1], array[high] = array[high], array[i + 1]
    draw_array(screen, array, {i + 1: (0, 0, 255), high: (255, 0, 0)})  # Azul para pivot
    pygame.time.delay(50)
    
    return i + 1

# Test básico para ejecutar el archivo directamente
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Visualización Quick Sort")
    
    array = [random.randint(10, 400) for _ in range(20)]  # Generar 20 números aleatorios
    quick_sort(array, screen)
    
    # Esperar a que el usuario cierre la ventana
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
