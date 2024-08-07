import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from scene_manager import SceneManager

def main():
    pygame.init()
    info = pygame.display.Info()
    display = (info.current_w, info.current_h)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL | pygame.FULLSCREEN)

    scene_manager = SceneManager()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    scene_manager.switch_visualization()
                elif event.key == pygame.K_UP:
                    scene_manager.increase_intensity()
                elif event.key == pygame.K_DOWN:
                    scene_manager.decrease_intensity()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        scene_manager.update()
        scene_manager.render()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
