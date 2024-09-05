import pygame
import random

# Función de visualización
def draw_array(screen, array, color_positions=None, clear_bg=True):
    if clear_bg:
        screen.fill((0, 0, 0))
    
    if color_positions is None:
        color_positions = {}
    
    bar_width = screen.get_width() // len(array)
    max_height = screen.get_height()

    for i, val in enumerate(array):
        color = color_positions.get(i, (255, 255, 255))  # Blanco por defecto
        bar_height = int(val / max(array) * max_height)
        pygame.draw.rect(screen, color, pygame.Rect(i * bar_width, max_height - bar_height, bar_width, bar_height))

      
    font = pygame.font.Font(None, 36)  
    text = font.render("Insertion Sort", True, (255, 255, 255))  
    screen.blit(text, (10, 10))  

    pygame.display.update()

def insertion_sort(array, screen):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            draw_array(screen, array, {j + 1: (255, 0, 0), j: (0, 255, 0)})  # Rojo y Verde para comparar
            pygame.time.delay(50)  # Añadir un pequeño retraso para visualización
            j -= 1
        array[j + 1] = key
        draw_array(screen, array, {j + 1: (0, 0, 255)})  # Azul para indicar la posición ordenada
        pygame.time.delay(50)
    return array

# Test básico dentro del archivo
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Visualización Insertion Sort")
    
    array = [random.randint(10, 400) for _ in range(20)]  # Generar 20 números aleatorios
    insertion_sort(array, screen)
    
    # Esperar a que el usuario cierre la ventana
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
