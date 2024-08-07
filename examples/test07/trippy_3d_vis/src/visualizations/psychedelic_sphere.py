import math
from OpenGL.GL import *
from OpenGL.GLU import *

class PsychedelicSphereVis:
    def __init__(self):
        self.rotation = 0
        self.quadric = gluNewQuadric()
        self.time = 0

    def update(self, beat_intensity):
        self.rotation += 1 + beat_intensity * 5
        self.time += 0.05

    def render(self):
        glPushMatrix()
        glRotatef(self.rotation, 0, 1, 0)

        for i in range(20):
            glPushMatrix()
            angle = i / 20 * 2 * math.pi
            x = math.sin(angle + self.time) * 0.5
            y = math.cos(angle + self.time) * 0.5
            z = math.sin(self.time * 2) * 0.2
            glTranslatef(x, y, z)
            r = (math.sin(self.time + i * 0.1) + 1) / 2
            g = (math.cos(self.time + i * 0.1) + 1) / 2
            b = (math.sin(self.time * 2 + i * 0.1) + 1) / 2
            glColor3f(r, g, b)
            gluSphere(self.quadric, 0.05 + math.sin(self.time + i) * 0.03, 16, 16)
            glPopMatrix()

        glColor3f(1, 1, 1)
        gluSphere(self.quadric, 0.3, 32, 32)
        glPopMatrix()
    def __init__(self):
        self.rotation = 0
        self.quadric = gluNewQuadric()

    def update(self):
        self.rotation += 1

    def render(self):
        glPushMatrix()
        glRotatef(self.rotation, 0, 1, 0)
        glColor3f(1, 1, 1)
        
        for i in range(10):
            glPushMatrix()
            glRotatef(i * 36, 0, 1, 0)
            glTranslatef(0.5, 0, 0)
            glColor3f(math.sin(i * 0.1), math.cos(i * 0.1), math.sin(i * 0.2))
            gluSphere(self.quadric, 0.1, 32, 32)
            glPopMatrix()

        gluSphere(self.quadric, 0.5, 32, 32)
        glPopMatrix()