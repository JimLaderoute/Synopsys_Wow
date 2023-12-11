import sys
import os
import pygame
import math

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
    clock =  pygame.time.Clock()

    letter_s = list (
        (
            (-0.6, 0.5),
            (-0.4, 1),
            (0.6, 1),
            (0.6, 0),
            (-0.4, 0),
            (-0.4, -1),
            (0.6, -1),
        )
    )
#    for i in range(len(letter_s)): letter_s[i] = ( letter_s[i][0] -0.40, letter_s[i][1] )
#    letter_s = [(p[0]-.4, p[1]) for p in letter_s]
#    print(letter_s)

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

    xscale = 20
    yscale = 40
    theta = 0
    seperation = 20

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
    
        surface.fill((0, 0, 0))
    
        xscale = math.sin(theta) * 20.0
        yscale = math.cos(theta) * 20.0

        #pygame.draw.circle(surface, color, (320, 240), 75, width=1)
        s1 = adjust_letter(letter_s, xscale, yscale,  seperation*1,  200)
        y1 = adjust_letter(letter_y, xscale, yscale,  seperation*4,  200)
        n1 = adjust_letter(letter_n, xscale, yscale,  seperation*7,  200)
        o1 = adjust_letter(letter_o, xscale, yscale,  seperation*10, 200)
        p1 = adjust_letter(letter_p, xscale, yscale,  seperation*13, 200)
        s2 = adjust_letter(letter_s, xscale, yscale,  seperation*16, 200)
        y2 = adjust_letter(letter_y, xscale, yscale,  seperation*19, 200)
        s3 = adjust_letter(letter_s, xscale, yscale,  seperation*22, 200)

   
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

        theta += 0.1
        #yscale = cos(theta)

#        xscale += multx
#        if xscale > 46:
#            multx = -1*multx
#        elif xscale < 10:
#            multx = -1 * multx

        clock.tick(30)

    pygame.quit()
    exit(0)

def adjust_letter(letter, xscale, yscale, xoffset=0, yoffset=0):
    rletter = letter.copy()
    for i in range(len(rletter)):
        rletter[i] = (rletter[i][0] * xscale + xoffset, rletter[i][1] * yscale + yoffset)
    return rletter

if __name__ == "__main__":
    main( sys.argv )