import pygame
import random
import sys
from insertionsort import insertion_sort
from bubblesort import bubble_sort_visual
from quicksort import quick_sort
from mergesort import merge_sort


# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Dibujar el menú en la pantalla
def draw_menu():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 36)
    title = font.render("Selecciona un Algoritmo de Ordenamiento", True, WHITE)
    bubble_sort_text = font.render("1. Bubble Sort", True, WHITE)
    quick_sort_text = font.render("2. Quick Sort", True, WHITE)
    merge_sort_text = font.render("3. Merge Sort", True, WHITE)
    insertion_sort_text = font.render("4. Insertion Sort", True, WHITE)
    exit_text = font.render("5. Exit", True, WHITE)

    font = pygame.font.Font(None, 36)  
    text = font.render("Creado por Fhermin", True, (255, 255, 255))  
    screen.blit(text, (width -(text.get_width() + 10), height - 40))  
    
    screen.blit(title, (width // 2 - title.get_width() // 2, 50))
    screen.blit(bubble_sort_text, (width // 2 - bubble_sort_text.get_width() // 2, 150))
    screen.blit(quick_sort_text, (width // 2 - quick_sort_text.get_width() // 2, 200))
    screen.blit(merge_sort_text, (width // 2 - merge_sort_text.get_width() // 2, 250))
    screen.blit(insertion_sort_text, (width // 2 - insertion_sort_text.get_width() // 2, 300))
    screen.blit(exit_text, (width // 2 - exit_text.get_width() // 2, 350))
    pygame.display.flip()

# Generar un array aleatorio para ordenar
def generate_random_array(size=20):
    return [random.randint(1, 100) for _ in range(size)]

# Bucle principal
def main():
    running = True
    selected_algorithm = None
    
    while running:
        draw_menu()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Bubble Sort
                    selected_algorithm = "bubble_sort"
                elif event.key == pygame.K_2:  # Quick Sort
                    selected_algorithm = "quick_sort"
                elif event.key == pygame.K_3:  # Merge Sort
                    selected_algorithm = "merge_sort"
                elif event.key == pygame.K_4:  # Insertion Sort
                    selected_algorithm = "insertion_sort"
                elif event.key == pygame.K_5:  # Exit Button
                    selected_algorithm = "exit_lol"
        
        if selected_algorithm:
            array = generate_random_array()
            if selected_algorithm == "bubble_sort":
                bubble_sort_visual(array, screen, width, height)
            elif selected_algorithm == "quick_sort":
                quick_sort(array, screen)
            elif selected_algorithm == "merge_sort":
                merge_sort(array, screen)
            elif selected_algorithm == "insertion_sort":
                insertion_sort(array, screen)
            elif selected_algorithm == "exit_lol":
                pygame.quit()
            
            # Esperar a que el usuario presione 'Q' para volver al menú o cierre la ventana
            waiting_for_input = True
            while waiting_for_input:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:  # Volver al menú al presionar 'Q'
                            selected_algorithm = None
                            waiting_for_input = False
                        elif event.key == pygame.K_BACKSPACE:
                            selected_algorithm = None
                            waiting_for_input = False
                pygame.display.flip()

if __name__ == "__main__":
    pygame.display.set_caption("Algoritmos de Ordenamiento Fhermin")
    main()
    pygame.quit()
