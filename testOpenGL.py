import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *








verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )


#edges = [(x,y) for x in range(0,8) for y in range(0,8) if x!=y]
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )
edges = [(x,y) for x in range(0,8) for y in range(0,8) if x!= y ]


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])       
    glEnd()


def main():
    speed,x,y,z = 1, 0, 0 ,0
    pygame.init()
    user32 = ctypes.windll.user32
    screenSize =  user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    size = (screenSize)
    pygame.display.set_caption("Window")
    pygame.display.set_mode((size), pygame.FULLSCREEN|DOUBLEBUF|OPENGL)

    gluPerspective(45, (size[0]/size[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, - 5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == 274:
                    x+=1
                    if x>1:
                        x=1
                    #glRotatef(speed,1,0,0)
                elif event.key == 273:
                    x-=1
                    if x<-1:
                        x=-1
                    #glRotatef(speed,-1,0,0)
                elif event.key == 275:
                    z+=1
                    if z>1:
                        z=1
                    #glRotatef(speed,0,1,0)
                elif event.key == 276:
                    z-=1
                    if z<-1:
                        z=-1
                    #glRotatef(speed,0,-1,0)
                elif event.key == 113:
                    pygame.quit()
                    quit()

        glRotatef(speed, x, y, z)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
