
import time
import pygame
import numpy as np

color_bg = (10, 10, 10)
color_grid = (40, 40, 40)
color_alive = (255, 255, 255)
color_die = (170, 170, 170)
color_txt = (0, 0, 0)

pygame.init()

#cell update function
def update(screen, cells, size, with_progress = False):
    updated_cells = np.zeros([cells.shape[0], cells.shape[1]])

    for row, col in np.ndindex(cells.shape):
        #amount of neighbouring alive cells tells us whether it's alive in the next round
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col] # comma indexing equivalent to two parentheses
        color = color_bg if cells[row, col] == 0 else color_alive
    
        #determine the fate of each cell : 
        if cells[row, col] == 1:
            if alive < 2 or alive > 3: #death
                if witgit h_progress:
                    color = color_die
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = color_alive
        
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = color_alive
        
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return updated_cells


# On-screen text
def plot_info_msg(msg):
        my_font = pygame.font.SysFont('CourierNew', 80).render(msg, False, (255, 255, 255))
        my_font.set_colorkey(color_txt)
        return my_font


# Game initialisation function

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720)) #sets grid size

    cells = np.zeros((int(720/20), int(1280/20))) #opposite order dimensions to resolution
    screen.fill(color_grid)
 
    pygame.font.init()  # you have to call this at the start
    my_font = pygame.font.SysFont('CourierNew', 80)
    text_surface1 = my_font.render('Click to Continue', False, (255, 255, 255))
    text_surface2 = my_font.render('full screen:    f', False, (255, 255, 255))
    text_surface3 = my_font.render('play/pause:     SPACE', False, (255, 255, 255))
    text_surface4 = my_font.render('select cell:    CLICK', False, (255, 255, 255))
    rect1=text_surface1.get_rect()
    rect2=text_surface2.get_rect()
    rect3=text_surface3.get_rect()
    rect4=text_surface4.get_rect()
    screen.fill((0,0,0))
    screen.blit(text_surface1, (0, 0), rect1)
    screen.blit(text_surface2, (0, 100), rect2)
    screen.blit(text_surface3, (0, 200), rect3)
    screen.blit(text_surface4, (0, 300), rect4)


    #update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 20)
                    pygame.display.update()
                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
                    screen.fill(color_grid)
                    update(screen, cells, 20)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 20, pos[0] // 20] = 1 #update cell based on mouse position
                update(screen, cells, 20)
                pygame.display.update()
                
        screen.fill(color_grid)

        if running:
            cells = update(screen, cells, 20, with_progress = True)
            pygame.display.update()
        time.sleep(0.01)

if __name__ == '__main__':
    main()