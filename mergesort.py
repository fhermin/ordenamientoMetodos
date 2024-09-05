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

# Función de Merge Sort con visualización
def merge_sort(array, screen, start=0, end=None):
    if end is None:
        end = len(array)
    
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(array, screen, start, mid)
        merge_sort(array, screen, mid, end)
        merge(array, screen, start, mid, end)

def merge(array, screen, start, mid, end):
    left = array[start:mid]
    right = array[mid:end]
    
    i = 0
    j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        draw_array(screen, array, {k: (0, 255, 0)})  # Verde para mostrar la posición que está siendo actualizada
        pygame.time.delay(50)
        k += 1

    while i < len(left):
        array[k] = left[i]
        draw_array(screen, array, {k: (0, 0, 255)})  # Azul para las posiciones ya ordenadas de la izquierda
        pygame.time.delay(50)
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        draw_array(screen, array, {k: (255, 0, 0)})  # Rojo para las posiciones ya ordenadas de la derecha
        pygame.time.delay(50)
        j += 1
        k += 1

# Test básico dentro del archivo
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Visualización Merge Sort")
    
    array = [random.randint(10, 400) for _ in range(20)]  # Generar 20 números aleatorios
    merge_sort(array, screen)
    
    # Esperar a que el usuario cierre la ventana
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
