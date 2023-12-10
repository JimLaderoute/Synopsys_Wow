import sys
import os
import pygame

cwd = os.path.dirname(os.path.abspath(__file__))
append_path = cwd + "/../lib"

sys.path.append(append_path)
import jjl_3d as _3d


def main(argv):
    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("Synopsys")
    surface = pygame.display.set_mode((640, 480))
    color = (55, 255, 255)
    line_color = (255, 255, 255)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
    
        surface.fill((0, 0, 0))
    
        pygame.draw.circle(surface, color, (320, 240), 75)
    
        try:
            poly1
        except NameError:
            poly1 = list(((320, 240), (320, 340), (420, 340), (420, 240)))
        else:
            poly1[0] = (poly1[0][0] + 1, poly1[0][1] + 1)
            poly1[1] = (poly1[1][0] + 1, poly1[1][1] + 1)
            poly1[2] = (poly1[2][0] + 1, poly1[2][1] + 1)
            poly1[3] = (poly1[3][0] + 1, poly1[3][1] + 1)
                      
        pygame.draw.polygon(surface, color, poly1)
        
        try:
            start1
            start2
        except NameError:
            start1 = list((0, 10))
            start2 = list((0, 240))
        else:
            start1[0] += 1
            start1[1] += 1
            start2[0] += 1
            start2[1] += 1
        pygame.draw.line(surface, line_color, start1, start2)

        pygame.display.flip()
        pygame.display.update()
        pygame.time.delay(100)

    pygame.quit()
    exit(0)

    
if __name__ == "__main__":
    main( sys.argv )