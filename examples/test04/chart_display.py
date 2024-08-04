import pygame
import os

def show_and_save_chart(chart_path):
    pygame.init()

    # Load the image
    image = pygame.image.load(chart_path)

    # Get image dimensions
    width, height = image.get_size()

    # Create a window of the same size as the image
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Gold Spot Price Chart (Press 'Q' to quit)")

    # Display the image
    screen.blit(image, (0, 0))
    pygame.display.flip()

    # Keep the window open until it's closed or 'q' is pressed
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

    pygame.quit()

    print(f"Chart saved as: {os.path.abspath(chart_path)}")
