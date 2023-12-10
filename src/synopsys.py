import sys
import os
import pygame

cwd = os.path.dirname(os.path.abspath(__file__))
append_path = cwd + "/../lib"
sys.path.append(append_path)

def main(argv):
    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("Synopsys")
    surface = pygame.display.set_mode((640, 480))
    color = (55, 255, 255)
    line_color = (255, 255, 255)
    

    letter_s = list (
        (
            (-0.2, 0.5),
            (0, 1),
            (1, 1),
            (1, 0),
            (0, 0),
            (0, -1),
            (1, -1),
        )
    )
    letter_y = [
        (-1, -1),
        (0, 0),
        (1, -1),
        (0, 0),
        (0, 1),    
    ]
    letter_n = [
        (-1, 1),
        (-1, -1),
        (1, 1),
        (1, -1),
    ]
    letter_o = [
        (1, 0),
        (0.7071, 0.7071),
        (0, 1),
        (-0.7071, 0.7071),
        (-1, 0),
        (-0.7071, -0.7071),
        (0, -1),
        (0.7071, -0.7071),
        (1, 0)  # Closing point to complete the polygon
    ]
    letter_p = [
        (-1, 1),
        (-1, -1),
        (1, -1),
        (1, 0),
        (-1, 0),

    ]

    s1 = adjust_letter(letter_s, 20,    200)
    y1 = adjust_letter(letter_y, 20*4,  200)
    n1 = adjust_letter(letter_n, 20*7,  200)
    o1 = adjust_letter(letter_o, 20*10, 200)
    p1 = adjust_letter(letter_p, 20*13, 200)
    s2 = adjust_letter(letter_s, 20*16, 200)
    y2 = adjust_letter(letter_y, 20*19, 200)
    s3 = adjust_letter(letter_s, 20*22, 200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
    
        surface.fill((0, 0, 0))
    
        #pygame.draw.circle(surface, color, (320, 240), 75, width=1)
    
        pygame.draw.lines(surface, color, False, s1, width=1)                      
        pygame.draw.lines(surface, color, False, y1, width=1)
        pygame.draw.lines(surface, color, False, n1, width=1)
        pygame.draw.lines(surface, color, False, o1, width=1)
        pygame.draw.lines(surface, color, False, p1, width=1)
        pygame.draw.lines(surface, color, False, s2, width=1)
        pygame.draw.lines(surface, color, False, y2, width=1)
        pygame.draw.lines(surface, color, False, s3, width=1)


        pygame.display.flip()
        pygame.display.update()
        pygame.time.delay(100)


    pygame.quit()
    exit(0)

def adjust_letter(letter, xoffset=0, yoffset=0):
    rletter = letter.copy()
    for i in range(len(rletter)):
        rletter[i] = (rletter[i][0] * 20 + xoffset, rletter[i][1] * 20 + yoffset)
    return rletter

if __name__ == "__main__":
    main( sys.argv )